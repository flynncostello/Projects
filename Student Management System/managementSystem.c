# include <stdio.h>
# include <stdbool.h>
# include <strings.h>
# include <stdlib.h>
# include <math.h>
# include <string.h>


struct student_data {
    char first_name[50];
    char last_name[50];
    char dob[50];
    char country[50];
    char gender[50];
    char address[50];
    char studyLocation[50];
    char curStudentYear[50];
    char finishYear[50];
    char unitsofstudy[50];
};


void students_info_formatter(struct student_data student_struct, int student_num) {
    printf("\n\n-------------------------------------------------------------"
    "\nStudent %i:"
    "\n-------------------------------------------------------------"
    "\nFirst Name: %s"
    "\nLast Name: %s"
    "\nDOB: %s"
    "\nCountry of Residence: %s"
    "\nGender: %s"
    "\nCurrent Address: %s"
    "\nCurrent Study Location: %s"
    "\nCurrent Student Year: %s"
    "\nCompletion Year: %s"
    "\nUnits of Study: %s", student_num, student_struct.first_name, student_struct.last_name, student_struct.dob, student_struct.country, student_struct.gender, student_struct.address, student_struct.studyLocation, student_struct.curStudentYear, student_struct.finishYear, student_struct.unitsofstudy);
    }


void copyOriginalFile() { // Original in read mode
    FILE *original; // Re-assigning to ensure changes to file will be accounted for
    original = fopen("database.txt", "r");

    FILE *temp; // Re-assigning to ensure changes to file will be accounted for
    temp = fopen("temp_database.txt", "w");

    /// Adding original file text to new temp file ///
    char cur_line[500];
    while ((fgets(cur_line, 500, original)) != NULL){
        fputs(cur_line, temp);
    
    }
    fclose(original);
    fclose(temp);
}


void addingAlteredLine(int alter_details_num, FILE *original_new, char *info_array[10], char formatter[]) {
    
    //printf("%s", formatter);
    
    switch (alter_details_num) {
        case 1:
            //printf("1");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new first name: ");
            char new_first_name[50];
            fgets(new_first_name, 50, stdin);
            new_first_name[strlen(new_first_name) - 1] = '\0';
            fprintf(original_new, formatter, new_first_name, info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        
        case 2:
            //printf("2");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new last name: ");
            char new_last_name[50];
            fgets(new_last_name, 50, stdin);
            new_last_name[strlen(new_last_name) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0], new_last_name, info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;

        case 3:
            //printf("3");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new date of birth (dd/mm/yyyy): ");
            char new_dob[50];
            fgets(new_dob, 50, stdin);
            new_dob[strlen(new_dob) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0], info_array[1], new_dob, info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;

        case 4:
            //printf("4");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new country of residence: ");
            char new_country[50];
            fgets(new_country, 50, stdin);
            new_country[strlen(new_country) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], new_country, info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        
        case 5:
            //printf("5");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new gender (male, female, other): ");
            char new_gender[50];
            fgets(new_gender, 50, stdin);
            new_gender[strlen(new_gender) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], new_gender, info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        
        case 6:
            //printf("6");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new address: ");
            char new_address[50];
            fgets(new_address, 50, stdin);
            new_address[strlen(new_address) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], new_address, info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        
        case 7:
            //printf("7");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new study location (domestic or abroad): ");
            char new_studyLocation[50];
            fgets(new_studyLocation, 50, stdin);
            new_studyLocation[strlen(new_studyLocation) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0] , info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], new_studyLocation, info_array[7], info_array[8], info_array[9]);
            break;
        
        case 8:
            //printf("8");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new student year (e.g., First Year): ");
            char new_studentYear[50];
            fgets(new_studentYear, 50, stdin);
            new_studentYear[strlen(new_studentYear) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], new_studentYear, info_array[8], info_array[9]);
            break;
        
        case 9:
            //printf("9");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new university finishing year: ");
            char new_finishYear[50];
            fgets(new_finishYear, 50, stdin);
            new_finishYear[strlen(new_finishYear) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], new_finishYear, info_array[9]);
            break;
        
        case 10:
            //printf("10");

            printf("\n----------------------------------------------------------------------------------------------------------");
            printf("\nEnter new units of study (e.g., INFO1110, INFO1111, BUSS1000, BUS1020,...): ");
            char new_unitsOfStudy[50];
            fgets(new_unitsOfStudy, 50, stdin);
            new_unitsOfStudy[strlen(new_unitsOfStudy) - 1] = '\0';
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], new_unitsOfStudy);
            break;
    }
    
}



char password[50] = "password";

bool run_program = true;



int main() {
    // OPENING FILE //
    FILE *databaseptr;
    databaseptr = fopen("database.txt", "r");

    if (databaseptr != NULL) { // Database file exists
        ///////////////////////////////
        ////////// MAIN MENU //////////
        ///////////////////////////////
        while (run_program) {
            printf(
            "\n**************************************************************************"
            "\n**************************************************************************"
            "\n***                                                                    ***"
            "\n***           ===== Student Record Management System =====             ***"                                                                                        
            "\n***                                                                    ***"
            "\n***                        By Flynn Costello                           ***"                          
            "\n***                                                                    ***"
            "\n***           Options:                                                 ***"                        
            "\n***               1. Show All Student Information                      ***"                                           
            "\n***               2. Add New Student                                   ***"                                
            "\n***               3. Modify Student Information                        ***"                                                
            "\n***               4. Quit                                              ***"                
            "\n***                                                                    ***"      
            "\n***                                                                    ***"                                                                                                            
            "\n**************************************************************************"
            "\n**************************************************************************");

            int main_menu_choice;
            printf("\n\n> ");
            scanf("%i", &main_menu_choice);
            getchar();

            FILE *databaseptr; // Re-assigning to ensure changes to file will be accounted for
            databaseptr = fopen("database.txt", "r");

            switch(main_menu_choice) {
                case 1:
                    // Option 1: PRINTING ENTIRE CONTENTS OF DATABASE FILE //
                    
                    printf("\n----------------------------------------------------------------------------------------------------------");
                    printf("\nEnter staff password: ");
                    char inputted_password[50];
                    fgets(inputted_password, 50, stdin);
                    inputted_password[strlen(inputted_password) - 1] = '\0';
                    
                    if (strcmp(inputted_password, password) != 0) {
                        printf("----------------------------------------------------------------------------------------------------------");
                        printf("\nPASSWORD DENIED. Redirecting back to home screen...");
                        printf("\n----------------------------------------------------------------------------------------------------------\n\n");
                    } else { // Valid password
                        printf("----------------------------------------------------------------------------------------------------------");
                        printf("\nPASSWORD ACCEPTED. Now printing entire student database");
                        printf("\n----------------------------------------------------------------------------------------------------------");

                        // Once password is accepted all student data is outputted to terminal //

                        printf("\n\n\n\t*****************************************");
                        printf("\n\t*           Student Database            *");
                        printf("\n\t*****************************************");

                        int student_num = 1;
                        const int MAX_LENGTH = 500;
                        char cur_entry[MAX_LENGTH]; // Each students data is held in here as one long string

                        // LOOPING THROUGH ENTIRE FILE //

                        while (fgets(cur_entry, MAX_LENGTH, databaseptr)) {
                            //printf("\nXXXXXXXXXX\n\n");
                            char *info_array[10]; // Needs to be a pointer as the tokens being collected are stored as pointers
                            char *token;
                            char *copy_string = cur_entry; // Need to copy string so original string doesn't get altered
                            
                            // LOOPING THROUGH CURRENT LINE AND ASSIGNING INFO TO ARRAY INDEXES //
                            int i = 0;
                            while ((token = strtok_r(copy_string, "$", &copy_string))) {
                                info_array[i] = token;
                                i++;
                            }

                            // LOOPING THROUGH ARRAY AND ASSIGNING VALUES TO NEW STRUCTURE //
                            struct student_data cur_student_struct;

                            strcpy(cur_student_struct.first_name, info_array[0]);
                            strcpy(cur_student_struct.last_name, info_array[1]);
                            strcpy(cur_student_struct.dob, info_array[2]);
                            strcpy(cur_student_struct.country, info_array[3]);
                            strcpy(cur_student_struct.gender, info_array[4]);
                            strcpy(cur_student_struct.address, info_array[5]);
                            strcpy(cur_student_struct.studyLocation, info_array[6]);
                            strcpy(cur_student_struct.curStudentYear, info_array[7]);
                            strcpy(cur_student_struct.finishYear, info_array[8]);
                            strcpy(cur_student_struct.unitsofstudy, info_array[9]);

                            // Printing current students information
                            //printf("\n\XXXXXXXXXX\n\n");
                            students_info_formatter(cur_student_struct, student_num);

                            student_num++;
                        }

                        printf("\n\n---------------------------------------------------------------------------------------------------------\n\n\n");
                    }
                    break;
                

                case 2: // Add new student
                    printf("\n----------------------------------------------------------------------------------------------------------");
                    printf("\nPlease enter your details below, ensuring you follow the formatting specifications:");
                    printf("\n----------------------------------------------------------------------------------------------------------\n\n");

                    printf("\n\t*****************************************");
                    printf("\n\t*            Student Details            *");
                    printf("\n\t*****************************************\n");

                    printf("\n\n----------------------------------------------------------------------------------------------------------");
                    char first_name[50];
                    printf("\n\nFirst Name: ");
                    fgets(first_name, 50, stdin);
                    first_name[strlen(first_name) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char last_name[50];
                    printf("\n\nLast Name: ");
                    fgets(last_name, 50, stdin);
                    last_name[strlen(last_name) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char dob[50];
                    printf("\n\nDate of Birth (dd/mm/yyyy): ");
                    fgets(dob, 50, stdin);
                    dob[strlen(dob) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char country[50];
                    printf("\n\nCountry of Residence: ");
                    fgets(country, 50, stdin);
                    country[strlen(country) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char gender[50];
                    printf("\n\nGender (Male, Female or Other): ");
                    fgets(gender, 50, stdin);
                    gender[strlen(gender) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char address[50];
                    printf("\n\nCurrent Address (house number and street, suburb, city): ");
                    fgets(address, 50, stdin);
                    address[strlen(address) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char studyLocation[50];
                    printf("\n\nCurrent Study Location (domestic or abroad): ");
                    fgets(studyLocation, 50, stdin);
                    studyLocation[strlen(studyLocation) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char curStudentYear[50];
                    printf("\n\nCurrent Student Year (e.g., First Year, Second Year, etc): ");
                    fgets(curStudentYear, 50, stdin);
                    curStudentYear[strlen(curStudentYear) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char finishYear[50];
                    printf("\n\nDegree Completion Year: ");
                    fgets(finishYear, 50, stdin);
                    finishYear[strlen(finishYear) - 1] = '\0';

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    char unitsofstudy[50];
                    printf("\n\nUnits of Study (unit1, unit2, unit3, unit4,...): ");
                    fgets(unitsofstudy, 50, stdin);
                    unitsofstudy[strlen(unitsofstudy) - 1] = '\0';


                    FILE *fptr; // FILE can be thought of as a data type
                    fptr = fopen("database.txt", "a");
                    fprintf(fptr, "\n%s$%s$%s$%s$%s$%s$%s$%s$%s$%s", first_name, last_name, dob, country, gender, address, studyLocation, curStudentYear, finishYear, unitsofstudy);
                    fclose(fptr);

                    printf("\n----------------------------------------------------------------------------------------------------------\n\n");

                    printf("**********************************************************************************************************\n\n");
                    char password[50];
                    printf("\n\nEnter the password you would like to have (Must be one word and no longer than 50 characters): ");
                    fgets(password, 50, stdin);
                    password[strlen(password) - 1] = '\0';



                    FILE *password_ptr; // Adding new student password to passwords file
                    password_ptr = fopen("passwords.txt", "a");
                    fprintf(password_ptr, "%s\n", password);
                    fclose(password_ptr);


                    break;



                case 3: // Modify student info
                    /// CHECKING FIRST NAME ///
                    printf("\n----------------------------------------------------------------------------------------------------------");
                    printf("\n\nPlease enter your first name: ");

                    char inputted_first_name[50];
                    fgets(inputted_first_name, 50, stdin);
                    inputted_first_name[strlen(inputted_first_name) - 1] = '\0';


                    int student_num = 1;
                    const int MAX_LENGTH = 500;
                    char cur_entry[MAX_LENGTH]; // Each students data is held in here as one long string
                    bool name_found = false;

                    // LOOPING THROUGH ENTIRE FILE //
                    int line_password_will_be_on = 0; // Used to find corresponding password for a specific name in the passwords.txt file

                    while (fgets(cur_entry, MAX_LENGTH, databaseptr)) {
                        //printf("\nXXXXXXXXXX\n\n");
                        char *info_array[10]; // Needs to be a pointer as the tokens being collected are stored as pointers
                        char *token;
                        char *copy_string = cur_entry; // Need to copy string so original string doesn't get altered
                        
                        // LOOPING THROUGH CURRENT LINE AND ASSIGNING INFO TO ARRAY INDEXES //
                        int i = 0;
                        while ((token = strtok_r(copy_string, "$", &copy_string))) {
                            info_array[i] = token;
                            i++;
                        }

                        // LOOPING THROUGH ARRAY AND ASSIGNING VALUES TO NEW STRUCTURE //
                        struct student_data cur_student_struct;

                        strcpy(cur_student_struct.first_name, info_array[0]);
                        strcpy(cur_student_struct.last_name, info_array[1]);
                        strcpy(cur_student_struct.dob, info_array[2]);
                        strcpy(cur_student_struct.country, info_array[3]);
                        strcpy(cur_student_struct.gender, info_array[4]);
                        strcpy(cur_student_struct.address, info_array[5]);
                        strcpy(cur_student_struct.studyLocation, info_array[6]);
                        strcpy(cur_student_struct.curStudentYear, info_array[7]);
                        strcpy(cur_student_struct.finishYear, info_array[8]);
                        strcpy(cur_student_struct.unitsofstudy, info_array[9]);
                        
                        line_password_will_be_on++;

                        if (strcmp(cur_student_struct.first_name, inputted_first_name) == 0) {
                            name_found = true; // Once name is found the loop and search can end
                            break;
                        }

                        student_num++;

                    }
                    if (name_found == false) { // Will not run if name is found. If name isn't found then program will return to main menu
                        printf("\n----------------------------------------------------------------------------------------------------------");                        
                        printf("\nName not found. Returning to home screen...");
                        printf("\n----------------------------------------------------------------------------------------------------------\n\n");
                        break;
                    }


                    /// CHECKING PASSWORD ///
                    FILE *passwords_ptr; // Making sure passwords file is up to date
                    passwords_ptr = fopen("passwords.txt", "r");
                    //printf("XXX %i XXX", line_password_will_be_on);

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    printf("\n\nPlease enter your password: ");
                    char user_inputted_password[50];
                    fgets(user_inputted_password, 50, stdin);
                    user_inputted_password[strlen(user_inputted_password) - 1] = '\0';
                    //printf("%c", user_inputted_password[strlen(user_inputted_password)]);

                    printf("\n----------------------------------------------------------------------------------------------------------");


                    // Checking inputted password against passwords in passwords.txt file to see if it aligns with the inputted name
                    const int NEW_MAX_LENGTH = 50;
                    char cur_password[MAX_LENGTH]; // Each students data is held in here as one long string
                    bool password_valid = false;

                    // LOOPING THROUGH ENTIRE FILE //
                    //printf("%i", line_password_will_be_on);

                    int cur_line = 1;
                    while (fgets(cur_password, MAX_LENGTH, passwords_ptr)) {
                        
                        if (cur_line == line_password_will_be_on) {
                            /*
                            printf("XXX%sXXX", cur_password);
                            printf("YYY%sYYY", user_inputted_password);

                            
                            char string1[20];
                            strcat(string1, &cur_password[strlen(cur_password) - 1]);
                            char string2[20] = "\n";

                            //printf("XXX%sXXX", string1);
                            //printf("XXX%sXXX", string2);
                            printf("%i", strcmp(string1, string2));

                            if (strcmp(string1, string2) == 0) {
                                //printf("OOO need to remove newline OOO");
                                cur_password[strlen(cur_password) - 1] = '\0';
                            }
                            */
                            cur_password[strlen(cur_password) - 1] = '\0';
                            //printf("XXX%sXXX", cur_password);
                            //printf("YYY%sYYY", user_inputted_password);

                            if (strcmp(cur_password, user_inputted_password) == 0) {
                                printf("\nPassword Accepted.");
                                printf("\n----------------------------------------------------------------------------------------------------------\n\n");
                                password_valid = true;
                            }
                        }
                        cur_line++;
                    }
                    fclose(passwords_ptr);

                    if (password_valid == false) {
                        printf("\nIncorrect Password. Returning to home menu...");
                        printf("\n----------------------------------------------------------------------------------------------------------\n\n");
                        break;
                    }



                    // Follows validation of student first name and password
                    printf("\t\t********************************************************");
                    printf("\n\t\t*            Update Student Details Process            *");
                    printf("\n\t\t********************************************************\n");


                    printf("\n\n----------------------------------------------------------------------------------------------------------");
                    printf("\nPlease choose one of the following details you would like to change:");
                    printf("\n----------------------------------------------------------------------------------------------------------");
                    printf("\n  1) First Name");
                    printf("\n  2) Second Name");
                    printf("\n  3) Date of Birth");
                    printf("\n  4) Country of Residence");
                    printf("\n  5) Gender");
                    printf("\n  6) Current Address");
                    printf("\n  7) Current Study Location");
                    printf("\n  8) Current Student Year");
                    printf("\n  9) Degree Completion Year");
                    printf("\n  10) Units of Study");
                    printf("\n----------------------------------------------------------------------------------------------------------");

                    int alter_details_num;
                    printf("\n> ");
                    scanf("%i", &alter_details_num);
                    getchar();

                    copyOriginalFile(); // Copying the database file to a temporary file


                    /// Adding temp file text back to original file but taking out the required line ///
                    FILE *original_new;
                    original_new = fopen("database.txt", "w");

                    FILE *temp_new; // Re-assigning to ensure changes to file will be accounted for
                    temp_new = fopen("temp_database.txt", "r");

                    char cur_line_new[500];
                    int count = 1;
                    //printf("XXX %i XXX", line_password_will_be_on);
                    // count = 1 for Flynn

                    while ((fgets(cur_line_new, 500, temp_new)) != NULL){
                        if (line_password_will_be_on != count) { // line_password_will_be_on works as this line is the same as the person's details in the database.txt file
                            fputs(cur_line_new, original_new); // Adding normal line of details back to original database.txt file
                            //printf("");

                        } else { // Line to be changed
                            //printf("THIS IS RUNNING XXXXX");
                            // Getting current line split up into array with each element being a different part of student details
                            char *info_array[10]; // Needs to be a pointer as the tokens being collected are stored as pointers
                            char *token;
                            //printf("%s", cur_line_new);
                            char *copy_string = cur_line_new; // Need to copy string so original string doesn't get altered
                            
                            // LOOPING THROUGH CURRENT LINE AND ASSIGNING INFO TO ARRAY INDEXES //
                            int i = 0;
                            while ((token = strtok_r(copy_string, "$", &copy_string))) {
                                info_array[i] = token;
                                i++;
                            }
                            
                            //printf("%s", info_array[0]);
                            // count = 1, original_new = database.txt file, info_array = array of length 10, each element is a string of info for student


                            if (count == 1) {
                                char formatter[] = "%s$%s$%s$%s$%s$%s$%s$%s$%s$%s";
                                //printf("XXX Flynn first line has run and formatter exlcudes the newline char XXX");
                                addingAlteredLine(alter_details_num, original_new, info_array, formatter);
                            } else {
                                char formatter[] = "%s$%s$%s$%s$%s$%s$%s$%s$%s$%s";
                                //printf("XXX Other line has printed XXX");
                                addingAlteredLine(alter_details_num, original_new, info_array, formatter);
                            }

                        }
                        count++;
                    }

                    fclose(original_new);
                    fclose(temp_new);

                    printf("\n----------------------------------------------------------------------------------------------------------");
                    printf("\nSuccessfully altered student details!");
                    printf("\n----------------------------------------------------------------------------------------------------------\n\n\n");

                    break;


                case 4:
                    printf("\n----------------------------------------------------------------------------------------------------------");
                    printf("\nNow exiting program...");
                    run_program = false;
                    break;


                default:
                    printf("\n----------------------------------------------------------------------------------------------------------");
                    printf("\nInvalid input. Try again...");
                    printf("\n----------------------------------------------------------------------------------------------------------\n\n");
                    break;
            }   
        }

        printf("\n----------------------------------------------------------------------------------------------------------");
        printf("\nThanks for using our student record management system!");
        printf("\n----------------------------------------------------------------------------------------------------------\n\n");
    
    } else {
        printf("Database file doesn't exist.");
    }


    return 0;
}


