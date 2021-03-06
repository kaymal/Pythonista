'''
Contacts

NOTE: Requires access to _contacts_.
'''

import contacts
import dialogs
from datetime import datetime
import operator

def main():
	days_list = []
	people = contacts.get_all_people()
	now = datetime.now()
	for p in people:
		b = p.birthday
		if not b:
			continue
		next_birthday = datetime(now.year, b.month, b.day)
		if next_birthday < now:
			next_birthday = datetime(now.year + 1, b.month, b.day)
		days = (next_birthday - now).days
		if days <= 7:
			days_list.append({'name': p.first_name, 'days': days})
	if not days_list:
		print('You don\'t have any birthdays in your address book.')
	else:
		days_list.sort(key=operator.itemgetter('days'))
		print('Upcoming Birthdays (for next 7 days)\n' + '=' * 40)
		for item in days_list:
			print('* %s in %i days' % (item['name'], item['days']))

if __name__ == '__main__':
	main()