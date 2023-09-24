# AmazonFlexWorker

Automate searching and accepting Amazon Flex Driver jobs.

This project aims to automate the process of picking up Amazon Flex driver jobs.
The ultimate goal of this project is to eliminate the need for drivers to manually search for jobs, allowing them to focus solely on completing the jobs assigned by the program.

**Note**: The Amazon Flex API was reverse-engineered by monitoring network traffic with Charles Proxy while using the Flex app. You may need to update the reverse-engineered API in this program if Amazon makes changes.

**Disclaimer 1**: Use this program at your own risk. The author is not responsible for any Flex account terminations or penalties imposed by Amazon as a result of its use.

**Disclaimer 2**: Running this program on AWS servers may not work, as Flex might block incoming connections from data centers to prevent large-scale automation. Consider using non-AWS data centers if needed.

## Usage

1. Ensure you have Python 3 installed (versions below 3 will not work).
2. Clone this repository to the machine where you intend to run the program (preferably connected to the internet via a wired connection).
3. Install dependencies using `pip`: `pip install -r requirements.txt`.
4. Set your `username` and `password` in the `config.json` file.
5. Customize the rest of the `config.json` file to match your job search preferences. It already contains some default settings. If you want to restrict your job search to specific warehouses, populate the `desiredWarehouses` field with internal warehouse IDs as strings. If not, leave it as an empty list.
6. You can also specify `desiredWeekdays` to restrict your job search to certain days of the week. Leave it as an empty list if not needed. Each string in `desiredWeekdays` must be a case-insensitive abbreviation of the day (e.g., "Sun" for Sunday, "monday" for Monday).
7. To find the internal warehouse IDs for the warehouses you're eligible for, run the following command: `python3 app.py getAllServiceAreas` or `python3 app.py --w`. You'll get a table of service areas and their corresponding internal warehouse IDs. Copy the IDs you want into the `desiredWarehouses` field in `config.json`.
8. Make sure to provide corresponding addresses for the warehouses in `desiredWarehousesAddress`, like this:

```json
{
  ...
  "desiredWarehouses": ["9c332725-c1be-405f-87c5-e7def58595f6", "5fa41ec8-44ae-4e91-8e48-7be008d72e8a"],
  ...
}
```

9. Make sureto provide `antiCaptchaToken` api this is need for when need to complete challanges 
