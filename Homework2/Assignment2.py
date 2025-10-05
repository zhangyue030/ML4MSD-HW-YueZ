import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bgdata = pd.read_json("Homework2/band_gap_data.json")
bgdata = bgdata.dropna(subset=['crystallinity', 'band_gap_type', 'exp_method', 'temperature_K', 'band_gap'])

bgdata = bgdata.loc[:, ['crystallinity', 'band_gap_type', 'exp_method', 'temperature_K', 'band_gap']]

np.random.seed(42)
shuffled = bgdata.sample(frac=1).reset_index(drop=True)
split = int(0.8 * len(shuffled))
train = shuffled[:split]
test = shuffled[split:]

crys_train = pd.get_dummies(train['crystallinity'], prefix='crys', drop_first=True)
band_train = pd.get_dummies(train['band_gap_type'], prefix='bandtype', drop_first=True)
exp_train  = pd.get_dummies(train['exp_method'], prefix='exp', drop_first=True)

crys_test = pd.get_dummies(test['crystallinity'], prefix='crys', drop_first=True)
band_test = pd.get_dummies(test['band_gap_type'], prefix='bandtype', drop_first=True)
exp_test  = pd.get_dummies(test['exp_method'], prefix='exp', drop_first=True)

crys_test = crys_test.reindex(columns=crys_train.columns, fill_value=0)
band_test = band_test.reindex(columns=band_train.columns, fill_value=0)
exp_test  = exp_test.reindex(columns=exp_train.columns, fill_value=0)

mean_T = train['temperature_K'].mean()
std_T = train['temperature_K'].std()
train['temperature_K'] = (train['temperature_K'] - mean_T) / std_T
test['temperature_K']  = (test['temperature_K']  - mean_T) / std_T

X_train = pd.concat([train[['temperature_K']], crys_train, band_train, exp_train], axis=1).to_numpy(dtype=float)
X_test  = pd.concat([test[['temperature_K']],  crys_test,  band_test,  exp_test],  axis=1).to_numpy(dtype=float)
y_train = train['band_gap'].to_numpy(dtype=float)
y_test  = test['band_gap'].to_numpy(dtype=float)

print(f" X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")

def ridge_regression(X, y, alpha):
    X = X.astype(float)
    X_bias = np.column_stack([np.ones(X.shape[0]), X])
    I = np.eye(X_bias.shape[1])
    I[0, 0] = 0  
    w = np.linalg.pinv(X_bias.T @ X_bias + alpha * I) @ X_bias.T @ y
    return w

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

corr = pd.concat(
    [pd.DataFrame(X_train, columns=['temperature_K'] + crys_train.columns.tolist() + band_train.columns.tolist() + exp_train.columns.tolist()),
     pd.Series(y_train, name='band_gap')],
    axis=1
).corr()

plt.figure(figsize=(10, 8))
plt.imshow(corr, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.title('Pearson Correlation Matrix')
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.tight_layout()
plt.show()

alphas = np.logspace(-4, 4, 100)
train_mse_list = []
test_mse_list = []

for alpha in alphas:
    w = ridge_regression(X_train, y_train, alpha)
    X_train_bias = np.column_stack([np.ones(X_train.shape[0]), X_train])
    X_test_bias = np.column_stack([np.ones(X_test.shape[0]), X_test])
    y_pred_train = X_train_bias @ w
    y_pred_test = X_test_bias @ w
    train_mse_list.append(mse(y_train, y_pred_train))
    test_mse_list.append(mse(y_test, y_pred_test))

plt.figure(figsize=(8, 6))
plt.plot(alphas, train_mse_list, label='Train MSE')
plt.plot(alphas, test_mse_list, label='Test MSE')
plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('MSE')
plt.title('MSE vs Alpha (Ridge Regression)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

best_idx = np.argmin(test_mse_list)
best_alpha = alphas[best_idx]
print(f"Best alpha = {best_alpha:.4f}")
print(f"Best test MSE = {test_mse_list[best_idx]:.4f}")

w_best = ridge_regression(X_train, y_train, best_alpha)
X_test_bias = np.column_stack([np.ones(X_test.shape[0]), X_test])
y_pred_best = X_test_bias @ w_best

plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred_best, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('True band_gap')
plt.ylabel('Predicted band_gap')
plt.title(f'True vs Predicted (alpha={best_alpha:.4f})')
plt.grid(True)
plt.tight_layout()
plt.show()

ss_res = np.sum((y_test - y_pred_best)**2)
ss_tot = np.sum((y_test - np.mean(y_test))**2)
r2 = 1 - ss_res / ss_tot
print(f"R^2 (test) = {r2:.4f}")


#The test error is lowest at α ≈ 4, which gives the best regularization.
#Test MSE decreases quickly when α increases from small values, then becomes flat instead of forming a clear U-shape.
#This means overfitting is not obvious, and regularization mainly stabilizes the model.
#The test R² is about 0.36, so the model explains around one-third of the variance.
#Predictions are generally lower than true values, especially for large band gaps, showing the model tends to predict near the average.
#This is likely because most features are categorical and the model is linear.
#Adding nonlinear or interaction features may improve the results.
