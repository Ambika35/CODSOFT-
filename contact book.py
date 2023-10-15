#TASK-3 Creating a user friendly contact book for storing name,phone no.,email and address for each contact , also allow user to add ,view,search,update,delete contact:
#@codsoft #codsoft #intership
def display_contact():
    print("your contact info is as follows");
    mycontact=contact.items();#items funtion will return you a key value pairs in a tuple form
    for key in mycontact:
        print(key);
contact={}; #declaring dictionary
while True:
    u_choice=int(input('''
                         press 1. add new contact
                         press 2. search contact
                         press 3. view contact
                         press 4. update contact
                         press 5. delete contact
                         press 6. exit'''));
    if u_choice==1:
        name=input("enter contact name");
        phone=int(input("enter phone no. of the contact"));
        email=input("enter email id of the contact");
        address=input("enter address of the contact");
        contact[name]=[[phone],[email],[address]];#as user has to put multiple values in the dictionary you can add such values in a single list as of a value for a key
    elif u_choice==2:
        search_name=input("enter name you want to search contact details for");
        if search_name in contact:
            print(search_name," 's contact details are",contact[search_name]);#for searching contact they would provide result accordingly
        else:
            print("contact not found");
    elif u_choice==3:
        if not contact:
            print("empty contact book");
        else:
            display_contact();#function call
    elif u_choice==4:
        edit_contact=input("enter the contact to be edited");
        if edit_contact in contact:
            phone=int(input("enter phone no. of the contact"));
            email=input("enter email id of the contact");
            address=input("enter the address for the contact");
            contact[edit_contact]=[[phone],[email],[address]];
            print("contact updated");
            display_contact();
        else:
            print("name not found");
    elif u_choice==5:
        del_contact=input("enter the contact to be deleted");
        if del_contact in contact:
            contact.pop(del_contact);#pop function in python helps in deleting values from the all type of sequences
            display_contact();
        else:
            print("name not found");
    else:
        break;
    
    
        
            
    
        
