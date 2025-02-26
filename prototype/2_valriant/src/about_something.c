
    #include <criterion/criterion.h>

    Test(about_control_statements, if_statements) {
        
    char char_variable = 'Q';
    int int_variable = 44;
    

        cr_assert_eq('Q', char_variable, "Some message1");
cr_assert_eq(44, int_variable, "Some message2");
    }
    