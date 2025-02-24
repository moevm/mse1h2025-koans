
    #include <criterion/criterion.h>

    Test(about_control_statements, if_statements) {
        
    char char_variable = 'U';
    int int_variable = 1;
    

        cr_assert_eq('U', char_variable, "Some message1");
cr_assert_eq(39, int_variable, "Some message2");
    }
    