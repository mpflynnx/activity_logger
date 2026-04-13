## Python Activity Task Logger

### Installation

- Click on green **<> Code** button on this GitHub repository and select **Download ZIP** to download the source files.
- Extract the **activity_logger-main.zip** archive
- Create a new folder to store the task logger source files, i.e **E:\tools** or similar
- Copy all the source files to the new folder

### Setting the Windows executable path
- Press keys **Win+x** then **y**, type in **Find a setting** search bar: **view advanced system settings**, then click on result of search.
- Click on **Environment Variables...** 
- Select **Path** under the **User Variables for **. 
- Click **Edit..** then click **New** then enter **E:\tools** or the location the source files are stored

### Usage examples
#### Logging a activity or task
- Open a **Command Prompt** or **Windows Terminal**
- At the > prompt type **log** then in double quotes **"the message you want to be logged"**
```bash
C:\Users\mpflynnx>log "This is my first task logged today."
✅ Logged: This is my first task logged today.
```
- The text is appended to a file named **activity_log.txt** also located at **E:\tools**
#### Viewing logged entries
- At the > prompt type **log --view**
```bash
C:\Users\mpflynnx>log --view
--- Recent Activity (Last 10) ---
2026-04-13 08:44:00 - This is my first task logged today.
```

#### Searching the log for a specific word
- At the > prompt type **log --search [word]** (note: case is ignored)
```bash
# Finds all logged tasks that include the word: windows, Windows or WINDOWS
C:\Users\mpflynnx>log --search windows
--- Search Results for 'windows' ---
2026-03-05 14:35:04.157 - Installed Nomacs on windows10 as a lightweight alternative for viewing PNG and images.
2026-03-05 14:40:51.972 - Installed SumatraPDF on windows10 as a lightweight alternative for viewing pdf and ebooks.
```
