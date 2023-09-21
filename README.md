This ia an expense-tracking web app for the book distribution company: Rumi Press, In django.
To run the project, First install dependencies from requirements.txt file:

$ pip install -r reqirements.txt

Now to import existing data from company spreadsheet that is in folder named "Spreadsheet" in project base dir, make postgres database:

$ sudo -i -u postgres
$ createdb <database_name>

Now go to psql command line:

$ psql -d <database_name> -U <user_name> -h <hostname>

Copy the existing data to database table of application model:

$ \COPY "<table_name>" FROM 'spreadsheet_dir' DELIMITER ',' CSV HEADER;

It is important to restart database table id to ability of adding new object of application model, So:

ALTER SEQUENCE "<table_name>_id_seq" RESTART WITH <number_of_rows + 1>;

It is ready to run.




