development = True

def get_mysql_uri():
	if development:
		return "mysql://root:@localhost/sig_link_shortener"
	else:
		return os.environ.get("NJTRANSIT_MYSQL_URI")
