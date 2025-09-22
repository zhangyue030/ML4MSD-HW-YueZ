### Summary of Interesting Observations

### Slicing

- Slicing uses the format [start:stop:step], where the start is inclusive and the stop is exclusive.

- Negative indices and negative steps allow convenient reverse operations like [::-1].

- A slice always produces a new object, so my_list[:] actually creates a copy.

- I also learned that slicing is powered by a slice object behind the scenes, which can even be used in custom classes.

### Pathlib

- Using pathlib.Path instead of plain strings makes file path operations easier and more readable.

- I found it useful that / is overloaded for path joining, and methods like .read_text(), .write_text(), .glob(), and .rglob() simplify many common tasks.

- Path objects automatically handle differences between Windows and Linux, so code becomes more cross-platform.

### File Modes (a, a+, w, w+, r+)

- The + symbol always means the file can be both read and written.

- a and a+ always append to the end, while w and w+ overwrite the file.

- r+ is unique: it allows reading and writing without clearing the file, but the file must exist already.

- I realized that these modes also determine the initial file pointer position (start vs. end).