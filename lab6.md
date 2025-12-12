**Laboratory Work 6**

Develop a class for working with a file. The class must contain basic methods such as: reading from and writing to the file, as well as the ability to append to the file (preserving the previous file content). The path and file name must be passed through the class constructor. When creating an instance of the class, it is necessary to check if the file exists. If such a file does not exist, generate an appropriate exception. During reading or writing to the file, if the file is corrupted or writing is impossible, generate an appropriate exception. You need to create your own custom exceptions to handle these errors. Additionally, develop a decorator for logging write, read, and file creation operations. This should be a parameterized decorator logged that accepts an exception and a mode as arguments. The mode can be "console" or "file". When an exception occurs in the decorated method, it is logged using the logging module. In console mode, logging occurs in the console, and in file mode, logging is written to a file.

Custom exceptions for clearly distinguishing file-related problems:

    File not found (FileNotFound).

    File is corrupted (problems with access or reading the file itself) (FileCorrupted).

File type for event logging - text

| Варіант | Тип файлу для читання/запису |
|:-------:|:----------------------------:|
|    5    |             csv              |
