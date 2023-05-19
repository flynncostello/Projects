/*
Enter the following, one after the other, in the terminal, to run the program:
gcc -o levelD_ex levelD.c `pkg-config --cflags --libs gtk+-3.0`
./levelD_ex
*/

# include <gtk/gtk.h>
# include <glib.h>
# include <stdio.h>
# include <stdbool.h>
# include <strings.h>
# include <stdlib.h>
# include <math.h>
# include <string.h>



// Used when altering student data
void copyOriginalFile() {
    // Original in read mode
    FILE *original = fopen("studentInfo.txt", "r");
    FILE *temp = fopen("temp_database.txt", "w");

    // Adding original file text to new temp file
    const int MAX_LINE_LENGTH = 500;
    char *cur_line = malloc(MAX_LINE_LENGTH * sizeof(char));

    while (fgets(cur_line, MAX_LINE_LENGTH, original) != NULL) {
        fputs(cur_line, temp);
    }

    fclose(original);
    fclose(temp);
    free(cur_line);
}

///// Callback function for the "delete-event" signal /////

gboolean on_window_delete_event(GtkWidget *widget, GdkEvent *event, gpointer data) {
    gtk_widget_hide(widget);  // Hide the window instead of destroying it
    return TRUE;  // Return TRUE to signal that the event has been handled
}


///// Callback function to return to the main menu /////
void return_to_main_page(GtkWidget *widget, gpointer data) {
    // Cast the data parameter to a GtkWindow
    GtkWindow *subpage = GTK_WINDOW(data);

    // Close the subpage window
    gtk_window_close(subpage);
}


///// Callback function used to output all student data in a tree table to the subpage window /////
void view_all_student_data_subpage(GtkWidget *widget, gpointer data) {
    // Create a new window for the subpage
    GtkWidget *subpage = gtk_window_new(GTK_WINDOW_TOPLEVEL); // creates subpage or the new window for the new page
    gtk_window_set_title(GTK_WINDOW(subpage), "Student Database");
    gtk_window_set_default_size(GTK_WINDOW(subpage), 2560, 1600);

    // Create a vertical box to hold the content
    GtkWidget *vertical_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 0); // Where data will be stored
    gtk_container_add(GTK_CONTAINER(subpage), vertical_box); 

    // Create a scrolled window to hold the treeview
    GtkWidget *scrolled_window = gtk_scrolled_window_new(NULL, NULL);
    // The GtkScrolledWindow widget is a container that provides horizontal and vertical scrolling for its child widget, which can be any other GTK widget
    gtk_widget_set_size_request(scrolled_window, 400, 400);
    gtk_scrolled_window_set_policy(GTK_SCROLLED_WINDOW(scrolled_window), GTK_POLICY_AUTOMATIC, GTK_POLICY_AUTOMATIC);
    gtk_box_pack_start(GTK_BOX(vertical_box), scrolled_window, TRUE, TRUE, 0);

    // Create a treeview to display the data
    GtkWidget *treeview = gtk_tree_view_new();
    // gtk_tree_view_new is a widget that allows users to display and manipulate hierarchical data in a tabular format
    gtk_container_add(GTK_CONTAINER(scrolled_window), treeview); // Adding the treeview table format to the window

    // Create the columns for the treeview
    GtkTreeViewColumn *column1 = gtk_tree_view_column_new_with_attributes("First Name", gtk_cell_renderer_text_new(), "text", 0, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column1);

    GtkTreeViewColumn *column2 = gtk_tree_view_column_new_with_attributes("Last Name", gtk_cell_renderer_text_new(), "text", 1, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column2);

    GtkTreeViewColumn *column3 = gtk_tree_view_column_new_with_attributes("Date of Birth", gtk_cell_renderer_text_new(), "text", 2, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column3);

    GtkTreeViewColumn *column4 = gtk_tree_view_column_new_with_attributes("Country of Residence", gtk_cell_renderer_text_new(), "text", 3, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column4);

    GtkTreeViewColumn *column5 = gtk_tree_view_column_new_with_attributes("Gender", gtk_cell_renderer_text_new(), "text", 4, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column5);
    
    GtkTreeViewColumn *column6 = gtk_tree_view_column_new_with_attributes("Current Address", gtk_cell_renderer_text_new(), "text", 5, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column6);

    GtkTreeViewColumn *column7 = gtk_tree_view_column_new_with_attributes("Study Location", gtk_cell_renderer_text_new(), "text", 6, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column7);

    GtkTreeViewColumn *column8 = gtk_tree_view_column_new_with_attributes("Current University Year", gtk_cell_renderer_text_new(), "text", 7, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column8);

    GtkTreeViewColumn *column9 = gtk_tree_view_column_new_with_attributes("Completion Year", gtk_cell_renderer_text_new(), "text", 8, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column9);

    GtkTreeViewColumn *column10 = gtk_tree_view_column_new_with_attributes("Units of Study", gtk_cell_renderer_text_new(), "text", 9, NULL);
    gtk_tree_view_append_column(GTK_TREE_VIEW(treeview), column10);


    // Create the list store to hold the data
    GtkListStore *list_store = gtk_list_store_new(10, G_TYPE_STRING, G_TYPE_STRING, G_TYPE_STRING, G_TYPE_STRING, G_TYPE_STRING, G_TYPE_STRING, G_TYPE_STRING, G_TYPE_STRING, G_TYPE_STRING, G_TYPE_STRING);
    // Add the data to the list store (example data shown)
    GtkTreeIter iter; // Looping through tree view table to add data

    /// LOOPING THROUGH studentInfo.txt to add all the students information to the table ///
    FILE *databaseptr; // Re-assigning to ensure changes to file will be accounted for
    databaseptr = fopen("studentInfo.txt", "r");

    int student_num = 1;
    const int MAX_LENGTH = 500;
    char cur_entry[MAX_LENGTH];

    while (fgets(cur_entry, MAX_LENGTH, databaseptr)) {
        char *info_array[10]; // Needs to be a pointer as the tokens being collected are stored as pointers
        char *token;
        char *copy_string = cur_entry; // Need to copy string so original string doesn't get altered
        
        // LOOPING THROUGH CURRENT LINE AND ASSIGNING INFO TO ARRAY INDEXES //
        int i = 0;
        while ((token = strtok_r(copy_string, "$", &copy_string))) {
            info_array[i] = token;
            i++;
        }
        //printf(info_array[0]);
        gtk_list_store_append(list_store, &iter);
        gtk_list_store_set(list_store, &iter, 0, info_array[0], 1, info_array[1], 2, info_array[2], 3, info_array[3], 4,info_array[4], 5, info_array[5], 6, info_array[6], 7, info_array[7], 8, info_array[8], 9, info_array[9], -1);
    }

    // Set the list store as the model for the treeview
    gtk_tree_view_set_model(GTK_TREE_VIEW(treeview), GTK_TREE_MODEL(list_store));

    // Create the return button which runs the "return_to_main_page" function when the return button is clicked
    GtkWidget *return_button = gtk_button_new_with_label("Return");
    g_signal_connect(G_OBJECT(return_button), "clicked", G_CALLBACK(return_to_main_page), subpage);
    gtk_container_add(GTK_CONTAINER(vertical_box), return_button); // Adding return button to page

    // Show all widgets
    gtk_widget_show_all(subpage);
}


// Defining new_details array
char new_details[11][50];

// Run when the button to confirm a new detail is clicked
void on_submit_button_clicked(GtkWidget *button, GtkWidget *textbox) {
    // Adding new detail to specific slot in new_details array
    const gchar *text = gtk_entry_get_text(GTK_ENTRY(textbox));
    //printf("Text: %s\n", text);
    int i = 0;
    while (i < 11) {
        if (strlen(new_details[i]) == 0) {
            strcpy(new_details[i], text);
            break;
        } else {
            i++;
        }
    }
}


// Creating buttons and text boxes for new details to be inputted
void get_details(GtkGrid *grid, char *promt_text, int row) {
    GtkWidget *label1 = gtk_label_new(promt_text);
    gtk_grid_attach(GTK_GRID(grid), label1, 0, row, 1, 1);

    // Area to enter text and input
    GtkWidget *textbox = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(grid), textbox, 1, row, 1, 1);

    // Clicking submit button
    GtkWidget *submit_button = gtk_button_new_with_label("Submit");
    gtk_grid_attach(GTK_GRID(grid), submit_button, 2, row, 1, 1);
    g_signal_connect(submit_button, "clicked", G_CALLBACK(on_submit_button_clicked), textbox);
}



void add_new_details_to_student_database(GtkButton *button, gpointer data) {
    FILE *fptr; // FILE can be thought of as a data type
    fptr = fopen("studentInfo.txt", "a");
    fprintf(fptr, "\n%s$%s$%s$%s$%s$%s$%s$%s$%s$%s", new_details[0], new_details[1], new_details[2], new_details[3], new_details[4], new_details[5], new_details[6], new_details[7], new_details[8], new_details[9]);
    fclose(fptr);

    FILE *password_ptr; // Adding new student password to passwords file
    password_ptr = fopen("passwords.txt", "a");
    fprintf(password_ptr, "\n%s", new_details[10]);
    fclose(password_ptr);

    // Cast the data parameter to a GtkWindow
    GtkWindow *parent_window = GTK_WINDOW(data);

    // Create the subpage window
    GtkWidget *subpage = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(subpage), "");
    gtk_container_set_border_width(GTK_CONTAINER(subpage), 10);
    gtk_widget_set_size_request(subpage, 200, 50);

    // Creating box to store widgets in
    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(subpage), box);

    // MAIN LABEL
    GtkWidget *label = gtk_label_new("New Details Successfully Submitted!");
    gtk_container_add(GTK_CONTAINER(box), label); // Adding label to page

    g_signal_connect(subpage, "destroy", G_CALLBACK(on_window_delete_event), NULL);

    // Show the subpage window
    gtk_window_set_transient_for(GTK_WINDOW(subpage), parent_window);
    gtk_window_set_modal(GTK_WINDOW(subpage), TRUE);
    gtk_widget_show_all(subpage);
}


///// Callback function for the add new students info button /////
void add_new_student_button_subpage(GtkButton *button, gpointer data) {
    // Cast the data parameter to a GtkWindow
    GtkWindow *parent_window = GTK_WINDOW(data);

    // Create the subpage window
    GtkWidget *subpage = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(subpage), "Adding New Student Details");
    gtk_container_set_border_width(GTK_CONTAINER(subpage), 10);
    gtk_widget_set_size_request(subpage, 1000, 500);

    // Creating box to store widgets in
    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(subpage), box);

    // MAIN LABEL
    GtkWidget *label = gtk_label_new("Fill in the boxes below and press submit to confirm each detail. Once all fields have completed and confirmed, press the 'SUBMIT ALL DETAILS' button to finalise your information:\n");
    gtk_container_add(GTK_CONTAINER(box), label); // Adding label to page

    // Adding grid to the box - box is vertical with only 1 column - grid adds columns to each row
    GtkWidget *grid = gtk_grid_new();
    gtk_box_pack_start(GTK_BOX(box), grid, TRUE, TRUE, 0);

    // ENTERING NEW STUDENT DATA

    int category_num = 0;
    char promt_texts[11][100] = {
        "First Name: ", 
        "Last Name: ", 
        "DOB (dd/mm/yyyy): ", 
        "Country of Residence: ", 
        "Gender (Male, Female, or Other): ", 
        "Current Address: ", 
        "Current Study Location (Domestic or Abroad): ", 
        "Current Student Year (E.g. First Year): ", 
        "Completion Year: ", 
        "Units of Study (E.g. INFO1111, INFO1110, BUSS1000, BUSS1020): ", 
        "New Password: "
    };

    while (category_num < 11) {
        get_details(GTK_GRID(grid), promt_texts[category_num], category_num);
        category_num++;
    }

    // Submit all data button
    GtkWidget *final_submit_button = gtk_button_new_with_label("SUBMIT ALL DETAILS");
    g_signal_connect(G_OBJECT(final_submit_button), "clicked", G_CALLBACK(add_new_details_to_student_database), NULL);
    gtk_container_add(GTK_CONTAINER(box), final_submit_button); // Adding return button to page

    // RETURN BUTTON
    GtkWidget *return_button = gtk_button_new_with_label("Return");
    g_signal_connect(G_OBJECT(return_button), "clicked", G_CALLBACK(return_to_main_page), subpage);
    gtk_container_add(GTK_CONTAINER(box), return_button); // Adding return button to page

    // Show the subpage window
    gtk_window_set_transient_for(GTK_WINDOW(subpage), parent_window);
    gtk_window_set_modal(GTK_WINDOW(subpage), TRUE);
    gtk_widget_show_all(subpage);
}


char *inputted_first_name = NULL;
char *inputted_last_name = NULL;
char *inputted_password = NULL;
bool valid_user = false;

// The following three functinos are call-back functions used when the submit button is clicked 
// as the user inputs data to validate they are actually a student

void on_submit_first_name_clicked(GtkWidget *button, GtkWidget *textbox) {
    const gchar *text = gtk_entry_get_text(GTK_ENTRY(textbox));
    free(inputted_first_name);  // free previous memory if any
    inputted_first_name = malloc(strlen(text) + 1);
    strcpy(inputted_first_name, text);
    //printf("Inputted First Name: %s\n", inputted_first_name);
}

void on_submit_last_name_clicked(GtkWidget *button, GtkWidget *textbox) {
    const gchar *text = gtk_entry_get_text(GTK_ENTRY(textbox));
    free(inputted_last_name);  // free previous memory if any
    inputted_last_name = malloc(strlen(text) + 1);
    strcpy(inputted_last_name, text);
    //printf("Inputted Last Name: %s\n", inputted_last_name);
}

void on_submit_password_clicked(GtkWidget *button, GtkWidget *textbox) {
    const gchar *text = gtk_entry_get_text(GTK_ENTRY(textbox));
    free(inputted_password);  // free previous memory if any
    inputted_password = malloc(strlen(text) + 1);
    strcpy(inputted_password, text);
    //printf("Inputted Password: %s\n", inputted_password);
}

// Creating buttons and text boxes for new details to be inputted
void creating_buttons_for_user_validation(GtkGrid *grid, char *promt_text, int row) {
    GtkWidget *label1 = gtk_label_new(promt_text);
    gtk_grid_attach(GTK_GRID(grid), label1, 0, row, 1, 1);

    // Area to enter text and input
    GtkWidget *textbox = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(grid), textbox, 1, row, 1, 1);

    // Clicking submit button
    GtkWidget *submit_button = gtk_button_new_with_label("Submit");
    gtk_grid_attach(GTK_GRID(grid), submit_button, 2, row, 1, 1);
    if (row == 0) {
        g_signal_connect(submit_button, "clicked", G_CALLBACK(on_submit_first_name_clicked), textbox);
    } else if (row == 1) {
        g_signal_connect(submit_button, "clicked", G_CALLBACK(on_submit_last_name_clicked), textbox);
    } else {
        g_signal_connect(submit_button, "clicked", G_CALLBACK(on_submit_password_clicked), textbox);
    }
}   



// Global variable to store selected field
char *field_to_be_changed; // string of name of field to be changed
char *new_detail;
int new_detail_index; // The index of the detail to be changed starting with "first name" at index 0 --> going to index 9
int line_details_will_be_changed_on;
int file_length;

// Callback function for the confirm button of the COMBO BOX INFO
void on_confirm_button_clicked(GtkWidget *widget, gpointer data) {
    // Get the selected option from the combo box
    //printf("CONFIRMING COMBO BUTTON DETAIL!!!\n");
    GtkComboBox *combo_box = GTK_COMBO_BOX(data);
    gchar *selected_option = gtk_combo_box_text_get_active_text(GTK_COMBO_BOX_TEXT(combo_box));
    
    // Copy the selected option to the global variable
    field_to_be_changed = g_strdup(selected_option);

    //printf("FIELD TO BE CHANGED: %s\n", field_to_be_changed);

    // Free the memory used by the selected option string
    g_free(selected_option);

    // Copying index of choice
    new_detail_index = gtk_combo_box_get_active(combo_box);

    //printf("INDEX OF FIELD TO BE CHANGED: %i\n", new_detail_index);

}


void on_submit_new_detail(GtkWidget *button, GtkWidget *textbox) {
    const gchar *detail = gtk_entry_get_text(GTK_ENTRY(textbox));
    free(new_detail);  // free previous memory if any
    new_detail = malloc(strlen(detail) + 1);
    strcpy(new_detail, detail);

    //printf("NEW DETAIL %s\n", new_detail);
}


void create_altered_student_detail_string(FILE *original_new, char *info_array[10], char formatter[]) {
    char *final_formatter = malloc(strlen(formatter) + 2); // allocate memory for string
    strcpy(final_formatter, formatter);
    strcat(final_formatter, "\n");

    //printf("NEW DETAIL INDEX IN CURRENT LINE: %i\n", new_detail_index);
    switch (new_detail_index + 1) { // Needs +1 as cases start at 1 whilst new_detail_index starts at 0 like normal indexing
        case 1:
            fprintf(original_new, formatter, new_detail, info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        case 2:
            fprintf(original_new, formatter, info_array[0], new_detail, info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        case 3:
            fprintf(original_new, formatter, info_array[0], info_array[1], new_detail, info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        case 4:
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], new_detail, info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        case 5:
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], new_detail, info_array[5], info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        case 6:
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], new_detail, info_array[6], info_array[7], info_array[8], info_array[9]);
            break;
        case 7:
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], new_detail, info_array[7], info_array[8], info_array[9]);
            break;
        case 8:
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], new_detail, info_array[8], info_array[9]);
            break;
        case 9:
            fprintf(original_new, formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], new_detail, info_array[9]);
            break;
        case 10:
            //printf(formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], new_detail);
            fprintf(original_new, final_formatter, info_array[0], info_array[1], info_array[2], info_array[3], info_array[4], info_array[5], info_array[6], info_array[7], info_array[8], new_detail);
            break;
    }
    
}



void on_confirm_detail_changes(GtkButton *button, gpointer data) {
    //printf("\nCHANGING DETAILS NOW!!!\n");
    //printf("\nFIELD TO CHANGE: %s, NEW DETAIL: %s, LINE BEING CHANGED: %i\n", field_to_be_changed, new_detail, line_details_will_be_changed_on);

    copyOriginalFile(); // Copying the database file to a temporary file which we will read from to write it all back to the
    // Original studentInfo file, however with the alterations now included to a speicif students data

    /// Adding temp file text back to original file but taking out the required line ///
    FILE *original_new;
    original_new = fopen("studentInfo.txt", "w"); // Instantly clears the file (but data is safe in temp_database.txt)

    FILE *temp_new; // Re-assigning to ensure changes to file will be accounted for
    temp_new = fopen("temp_database.txt", "r");

    char *cur_line_new = malloc(500 * sizeof(char));
    int count = 0; // Represents the current line within the student database we are looking at
    while ((fgets(cur_line_new, 500, temp_new)) != NULL) { // Getting new line from temp_database.txt
        if (line_details_will_be_changed_on != count) { // line_password_will_be_on is the index of the line to be changed
            fputs(cur_line_new, original_new); // Adding normal line of details back to original database.txt file

        } else { // Line to be changed
            // Getting current line split up into array with each element being a different part of student details
            char *info_array[10]; // Needs to be a pointer as the tokens being collected are stored as pointers
            char *token;
            char *copy_string = cur_line_new; // Need to copy string so original string doesn't get altered
            
            // LOOPING THROUGH CURRENT LINE AND ASSIGNING INFO TO ARRAY INDEXES //
            int i = 0;
            while ((token = strtok_r(copy_string, "$", &copy_string))) {
                info_array[i] = token;
                //printf("\n%s\n", token);
                i++;
            }
            
            // Process just makes a list of strings from the original long string
            char* new_detail_line = (char*) malloc(1000 * sizeof(char));
            char formatter[] = "%s$%s$%s$%s$%s$%s$%s$%s$%s$%s";
            create_altered_student_detail_string(original_new, info_array, formatter);
        }
        count++;
    }

    fclose(original_new);
    fclose(temp_new);


    // Add new window with confirmation message here
    // Cast the data parameter to a GtkWindow
    GtkWindow *parent_window = GTK_WINDOW(data);

    // Create the subpage window
    GtkWidget *subpage = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(subpage), "");
    gtk_container_set_border_width(GTK_CONTAINER(subpage), 10);
    gtk_widget_set_size_request(subpage, 200, 50);

    // Creating box to store widgets in
    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(subpage), box);

    // MAIN LABEL
    GtkWidget *label = gtk_label_new("Details Successfully Altered!");
    gtk_container_add(GTK_CONTAINER(box), label); // Adding label to page

    g_signal_connect(subpage, "destroy", G_CALLBACK(on_window_delete_event), NULL);

    // Show the subpage window
    gtk_window_set_transient_for(GTK_WINDOW(subpage), parent_window);
    gtk_window_set_modal(GTK_WINDOW(subpage), TRUE);
    gtk_widget_show_all(subpage);
}


// Callback function used when the confirm details for login are entered
void on_confirm_login_details_button_pressed(GtkButton *button, gpointer data) {
    bool first_name_valid = false;
    bool last_name_valid = false;
    bool password_valid = false;
    valid_user = false;

    if (inputted_first_name != NULL && inputted_last_name != NULL && inputted_password != NULL) {
        //printf("ZZZ INSIDE THE IF STATEMENT!!!\n");
        // Checking first name
        FILE *databaseptr; // Re-assigning to ensure changes to file will be accounted for
        databaseptr = fopen("studentInfo.txt", "r");

        int row = 0;
        const int MAX_LENGTH = 500;
        char cur_entry[MAX_LENGTH]; // Each students data is held in here as one long string
        char *array_with_cur_students_first_and_last_name[2];

        // LOOPING THROUGH ENTIRE FILE //
        int line_password_will_be_on = 0; // Used to find corresponding password for a specific name in the passwords.txt file

        while (fgets(cur_entry, MAX_LENGTH, databaseptr)) {
            char *token;
            char *copy_string = cur_entry; // Need to copy string so original string doesn't get altered
            
            // LOOPING THROUGH CURRENT LINE AND ASSIGNING INFO TO ARRAY INDEXES //
            int i = 0;
            while ((token = strtok_r(copy_string, "$", &copy_string)) && i < 2) {
                array_with_cur_students_first_and_last_name[i] = malloc(strlen(token) + 1);
                strcpy(array_with_cur_students_first_and_last_name[i], token);
                i++;
            }

            if (strcmp(array_with_cur_students_first_and_last_name[0], inputted_first_name) == 0 && strcmp(array_with_cur_students_first_and_last_name[1], inputted_last_name) == 0) {
                first_name_valid = true; // Once name is found the loop and search can end
                last_name_valid = true;
                line_details_will_be_changed_on = line_password_will_be_on;
                break;
            }

            line_password_will_be_on++; // Checking new line in file
        }

        fclose(databaseptr);

        /*
        if (first_name_valid == true && last_name_valid == true) {
            printf("XXX First and Last Name are valid XXX\n");
        }
        */
        
        

        FILE *passwords_ptr;
        passwords_ptr = fopen("passwords.txt", "r");
        //printf("LINE PASSWORD ON : %i\n", line_details_will_be_changed_on); // The index in the array of entries (for a, a, a its index 3)
        // Checking inputted password against passwords in passwords.txt file to see if it aligns with the inputted name
        const int NEW_MAX_LENGTH = 50;
        char *cur_password = malloc(NEW_MAX_LENGTH * sizeof(char)); // Allocate memory for the current password
        int cur_line = 0;
        while (fgets(cur_password, NEW_MAX_LENGTH, passwords_ptr)) {
            //printf("Entered Password: %s, Current Password were checking: %s\n", inputted_password, cur_password);
            if (cur_line == line_password_will_be_on) {
                if (!feof(passwords_ptr)) {
                    cur_password[strlen(cur_password) - 1] = '\0';
                }
                //printf("PASSWORD IN FILE: %s\n", cur_password);
                //printf("PASSWORD USER INPUTTED: %s\n", inputted_password);            

                if (strcmp(cur_password, inputted_password) == 0) {
                    password_valid = true;
                }
            }
            cur_line++;
        }
        fclose(passwords_ptr);
        free(cur_password); // Free the memory allocated for cur_password

        if (first_name_valid == true && last_name_valid == true && password_valid == true) {
            //printf("MAKING VALID USER TRUE!!!\n");
            valid_user = true;
        }
        
        /*
        if (password_valid == true) {
            printf("YYY Password is Valid YYY\n");
        }
        if (valid_user == true) {
            printf("USER IS VALID ALL OVER\n");
        }
        */
        
    }

    // Creating new smaller window to tell user if their information entered is valid or not
    GtkWindow *parent_window = GTK_WINDOW(data);
    GtkWidget *subpage = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(subpage), "");
    gtk_container_set_border_width(GTK_CONTAINER(subpage), 10);
    gtk_widget_set_size_request(subpage, 200, 50);
    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(subpage), box);
    
    GtkWidget *labelC;
    if (valid_user == true) {
        labelC = gtk_label_new("Details are VALID. You may now choose the detail you would like to alter and the new value this field will hold for your own personal information.");
        gtk_container_add(GTK_CONTAINER(box), labelC); // Adding label to page
        g_signal_connect(subpage, "destroy", G_CALLBACK(on_window_delete_event), NULL);


        // Adding grid to the box - box is vertical with only 1 column - grid adds columns to each row
        GtkWidget *grid = gtk_grid_new();
        gtk_box_pack_start(GTK_BOX(box), grid, TRUE, TRUE, 0);


        ///// CHOOSING THE FIELD THEY WOULD LIKE TO ALTER /////

        GtkWidget *text = gtk_label_new("Choose the detail you would like to alter:");
        gtk_grid_attach(GTK_GRID(grid), text, 0, 0, 1, 1);

        GtkWidget *combo_box = gtk_combo_box_text_new();
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "First Name");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Last Name");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Date of Birth (dd/mm/yyyy)");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Country of Residence");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Gender (Male, Female or Other)");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Current Address (house number and street, suburb, city)");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Current Study Location (domestic or abroad)");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Current Student Year (e.g., First Year, Second Year, etc)");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Degree Completion Year");
        gtk_combo_box_text_append_text(GTK_COMBO_BOX_TEXT(combo_box), "Units of Study (unit1, unit2, unit3, unit4,...)");
        gtk_grid_attach(GTK_GRID(grid), combo_box, 1, 0, 1, 1);
      

        // Clicking submit button
        GtkWidget *submit_button = gtk_button_new_with_label("Submit");
        gtk_grid_attach(GTK_GRID(grid), submit_button, 2, 0, 1, 1);

        // Runs when the user clicks the submit button - this function just stores which field the user wants to change
        g_signal_connect(submit_button, "clicked", G_CALLBACK(on_confirm_button_clicked), combo_box);


        ///// CHOOSING WHAT THE NEW VALUE THE FIELD WILL HOLD WILL BE /////

        GtkWidget *new_detail_label = gtk_label_new("Enter the new detail for your chosen field: ");
        gtk_grid_attach(GTK_GRID(grid), new_detail_label, 0, 1, 1, 1);

        // Area to enter text and input
        GtkWidget *new_detail_textbox = gtk_entry_new();
        gtk_grid_attach(GTK_GRID(grid), new_detail_textbox, 1, 1, 1, 1);

        // Clicking submit button
        GtkWidget *submit_buttonB = gtk_button_new_with_label("Submit");
        gtk_grid_attach(GTK_GRID(grid), submit_buttonB, 2, 1, 1, 1);

        // Runs when the user clicks the submit button - this function just stores which field the user wants to change
        g_signal_connect(submit_buttonB, "clicked", G_CALLBACK(on_submit_new_detail), new_detail_textbox);

        // Button used to run alterations to details - uses row details are on (found earlier) to make changes
        GtkWidget *confirm_login_details_button = gtk_button_new_with_label("Confirm Changes");
        gtk_grid_attach(GTK_GRID(grid), confirm_login_details_button, 2, 4, 2, 1);
        g_signal_connect(G_OBJECT(confirm_login_details_button), "clicked", G_CALLBACK(on_confirm_detail_changes), NULL);

        // RETURN BUTTON
        GtkWidget *return_buttonC = gtk_button_new_with_label("Return");
        g_signal_connect(G_OBJECT(return_buttonC), "clicked", G_CALLBACK(return_to_main_page), subpage);
        gtk_container_add(GTK_CONTAINER(box), return_buttonC); // Adding return button to page


        // Show the subpage window
        gtk_window_set_transient_for(GTK_WINDOW(subpage), parent_window);
        gtk_window_set_modal(GTK_WINDOW(subpage), TRUE);
        gtk_widget_show_all(subpage);


    } else {
        labelC = gtk_label_new("Details are INVALID. Either your first name, last name, or password is incorrect. Please fix this issue before continuing.");
        gtk_container_add(GTK_CONTAINER(box), labelC); // Adding label to page
        g_signal_connect(subpage, "destroy", G_CALLBACK(on_window_delete_event), NULL);

        // Show the subpage window
        gtk_window_set_transient_for(GTK_WINDOW(subpage), parent_window);
        gtk_window_set_modal(GTK_WINDOW(subpage), TRUE);
        gtk_widget_show_all(subpage);
    }

}


///// Callback function for the edit existing students data button /////
void edit_existing_data_button_subpage(GtkButton *button, gpointer data) {
    // Cast the data parameter to a GtkWindow
    GtkWindow *parent_window = GTK_WINDOW(data);

    // Create the subpage window
    GtkWidget *subpage = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(subpage), "Editing Existing Student Information");
    gtk_container_set_border_width(GTK_CONTAINER(subpage), 10);
    gtk_widget_set_size_request(subpage, 1000, 500);

    // Adding Box to subpage
    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);

    // Create the label in the subpage
    GtkWidget *label = gtk_label_new("Please begin by entering your first and last name as well as your password. After you enter each detail make sure to press 'Submit', and once you complete all details make sure to press 'Confirm Log-In Details':");
    gtk_container_add(GTK_CONTAINER(box), label); // Adding label to page

    // Adding grid to the box - box is vertical with only 1 column - grid adds columns to each row
    GtkWidget *grid = gtk_grid_new();
    gtk_box_pack_start(GTK_BOX(box), grid, TRUE, TRUE, 0);

    int question_num = 0;
    char questions[3][50] = {"Enter first name: ", "Enter last name: ", "Enter password: "};

    while (question_num < 3) {
        //printf("1");
        creating_buttons_for_user_validation(GTK_GRID(grid), questions[question_num], question_num);
        question_num++;
    }

    // Button used to confirm the details enterd by user so that they can then alter their own details
    GtkWidget *confirm_login_details_button = gtk_button_new_with_label("Confirm Log-In Details");
    gtk_grid_attach(GTK_GRID(grid), confirm_login_details_button, 1, 4, 2, 1);
    g_signal_connect(G_OBJECT(confirm_login_details_button), "clicked", G_CALLBACK(on_confirm_login_details_button_pressed), NULL);

    // Create the "Return" button in the subpage
    GtkWidget *return_button = gtk_button_new_with_label("Return");
    g_signal_connect(G_OBJECT(return_button), "clicked", G_CALLBACK(return_to_main_page), subpage);
    gtk_container_add(GTK_CONTAINER(box), return_button); // Adding return button to page

    // Add the box to the subpage window
    gtk_container_add(GTK_CONTAINER(subpage), box); 

    // Show the subpage window
    gtk_window_set_transient_for(GTK_WINDOW(subpage), parent_window);
    gtk_window_set_modal(GTK_WINDOW(subpage), TRUE);
    gtk_widget_show_all(subpage);
    //printf("XXXX");

}


// Main Function - main window creation
int main(int argc, char *argv[]) {
    ///// INITIALISING ARGUMENTS /////
    gtk_init(&argc, &argv);

    ///// Create the main window /////
    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Student Database Management System");
    gtk_window_set_default_size(GTK_WINDOW(window), 1280, 800); // Window is default size of window on MacOS
    gtk_container_set_border_width(GTK_CONTAINER(window), 10); // Padding of 10 pixels on borders of screen

    ///// Create a main vertical box to hold everything /////
    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_container_add(GTK_CONTAINER(window), box);
    // "box" is where all the main menu's widgets and buttons are stored - it acts like a vertical table

    ////////// CREATING AND ADDING ALL WIDGETS ON MAIN PAGE //////////

    ///// CREATING WELCOME TEXT /////
    GtkWidget *label = gtk_label_new("Welcome to the Student Database Management System - By Flynn Costello\n\nUse the buttons below to choose what you would like do to:");
    gtk_box_pack_start(GTK_BOX(box), label, FALSE, FALSE, 5);

    ///// Add a button to view all student data /////
    GtkWidget *view_all_student_data_button = gtk_button_new_with_label("View Entire Student Database");
    gtk_widget_set_size_request(view_all_student_data_button, 100, 100);
    g_signal_connect(G_OBJECT(view_all_student_data_button), "clicked", G_CALLBACK(view_all_student_data_subpage), NULL);
    gtk_box_pack_start(GTK_BOX(box), view_all_student_data_button, FALSE, FALSE, 5);

    ///// Add a button to add new student details /////
    GtkWidget *add_new_student_button = gtk_button_new_with_label("Add New Student");
    gtk_widget_set_size_request(add_new_student_button, 100, 100);
    g_signal_connect(G_OBJECT(add_new_student_button), "clicked", G_CALLBACK(add_new_student_button_subpage), NULL);
    gtk_box_pack_start(GTK_BOX(box), add_new_student_button, FALSE, FALSE, 5);

    ///// Add a button to edit existing student details /////
    GtkWidget *edit_existing_data_button = gtk_button_new_with_label("Edit Existing Student Details");
    gtk_widget_set_size_request(edit_existing_data_button, 100, 100);
    g_signal_connect(G_OBJECT(edit_existing_data_button), "clicked", G_CALLBACK(edit_existing_data_button_subpage), NULL);
    gtk_box_pack_start(GTK_BOX(box), edit_existing_data_button, FALSE, FALSE, 5);

    ///// ADDING IMAGE TO BOTTOM OF WINDOW /////
    GdkPixbuf *pixbuf = gdk_pixbuf_new_from_file("logo.png", NULL);
    GtkWidget *image = gtk_image_new_from_pixbuf(pixbuf);
    gtk_image_set_pixel_size(GTK_IMAGE(image), 600);
    gtk_box_pack_start(GTK_BOX(box), image, FALSE, FALSE, 5);

    ///// ENDS PROGRAM WHEN EXIT IS CLICKED BY USER - Connects delete-event to corresponding callback function /////
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    ///// OUTPUTTING ALL WIDJETS AND BUTTONS TO WINDOW /////
    gtk_widget_show_all(window);

    ///// RUNNING MAIN GTK+ LOOP FOR PROGRAM /////    
    gtk_main();

    return 0;
}