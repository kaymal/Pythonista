'''
Contacts: Names and E-mails

NOTE: Requires access to _contacts_.
'''

import contacts

def main():
    people = contacts.get_all_people()
    
    for p in people :
        f_name = p.first_name
        l_name = p.last_name
        e_mail = p.email
        
        print(f_name + ' ' + l_name, end = ' : ')
        
        for e in e_mail:
            print(e[1])


if __name__ == '__main__':
	main()