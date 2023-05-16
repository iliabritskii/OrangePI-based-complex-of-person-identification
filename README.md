The programs in this repository are designed to configure a person identification software and hardware complex based on a microcomputer.

To create a hardware and software complex, a microcomputer and a video camera are required. It is recommended to use Linux as an operating system for the hardware and software complex.

The algorithm of the hardware and software complex:

• Allocation and saving to the queue for processing frames from the video stream on which a person is present.

• Processing of saved photos, calculating values for vectors based on points on a person's face.

• Checking for the presence of a person in the database.

• Record the time of the person's appearance in the report, in case of successful identification, and delete the photo.

• Moving the photo and further attaching it to the report, if the person has not been identified.

• Sending the report by e-mail at the time selected when configuring the hardware and software complex.

Some programs run each other when working, so you need to specify the paths to the files in the program code in accordance with the placement of programs in your directory.

Description of programs:

• add_new_people.ru - adding a new person to the database, launched from GUI_new_people.

• change_crontab.py - changes the time when the report is sent to the mail (launched from GUI_login_agmin).

• create_dataset.py - creates an empty file in the desired format for entering datasets (it starts when all data is deleted from the database).

• dataset – a file with reference data for comparison.

• faces_recognition.ru - processing of a saved photo and human recognition.

• GUI_login_admin.ru - GUI for email registration and time of receipt of reports (creates mail.txt and time.txt ).

• GUI_new_people.ru - GUI for adding new people to the database.

• GUI_remove_dataset.py - GUI for deleting the database.

• images_checker.sh – checking for photos added to the processing queue (it is necessary to automate the launch via Cron or another task scheduler).

• mail.txt – a text file that stores mail for sending reports.

• people_recognition.ru - recognition of the appearance of a person in the frame, takes a photo (works in the background constantly, you need to put in autorun via Cron or another task scheduler).

• remove.ru - deletes sent reports and photos of unidentified people.

• report.xlsx , report.csv files with the report.

• <url> - sending reports and photos to the mail

• table_creator.ru - creates files for reports after they are deleted (sent) (creates a report.xlsx and report.csv)

• time.txt – a text file that stores the selected time for sending reports.

• writer.ru - enters data about the identified person in the report

• white.jpg – used to add a white background for the inscription on photos with unidentified people.

• GUI_login_admin.desktop, GUI_new_people.desktop, GUI_remove_dataset.desktop – shortcuts for launching programs with a graphical interface.