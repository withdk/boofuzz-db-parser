"""
Work in progress....

Nice to be able to use CLI tools to analyse fuzz results in more detail.

TODO:
Process chunks in memory. This will be a much faster way than looping over steps.

DK @withdk
September 2020
"""
from boofuzz import fuzz_logger_db as boo

def get_test_cases(rowcount, type):
	for i in range(1,rowcount): # rowcount
		try:
			DTS = db.get_test_case_data(i)
			get_row_type(DTS,type)
		except:
			#print(f"Couldn't get row {i}")
			continue


def get_row_type(DTS, type): # row.steps
	""" DataTestStep.steps (list)
		types: info, error, send, receive, check (see boofuzz.helpers)

	Example:
	row.steps[]
	<class 'boofuzz.data_test_case.DataTestCase'>

	Returns a list of type DataTestStep:
	DataTestStep(
		type='info',
		description="Type: Bytes. Default value: b'clientHostName=DESKTOP-NN61BVC clientIp=172.16.10.129'. Case 1 of 49981 overall.",
		data=b'',
		timestamp='[2020-08-31 12:04:23,394]',
		truncated=0
	)
	"""
	for step in DTS.steps:
		if(step.type == type):
			print(step.data)
			#print(step[type])


db = boo.FuzzLoggerDbReader("boofuzz-results/run-2020-09-03T18-03-20.db")
query="select count(*) from steps"
#query="select * from steps"

# get rowcount
r = db.query(query, None)
rowcount = r.fetchone()[0]
# get receive data to have a more detailed look at results
# types: info, error, send, receive, check (see boofuzz.helpers)
get_test_cases(rowcount, "receive")

#get_row_type(DTS, "receive")

#steps_all_loop(row.steps)
#get_row_type(row.steps, 'receive')
