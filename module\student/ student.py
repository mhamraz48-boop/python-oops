class studentclass:
    def __init__(self):
        # Student details
        self.full_name = ""
        self.date_of_birth = ""
        self.age = 0
        self.gender = ""
        self.mobile_number = ""
        self.email_address = ""
        self.preferred_language = ""
        self.school_college_name = ""
        self.class_grade = ""
        self.board_curriculum = ""
        self.academic_year = ""
        self.subjects_tuition = []
        self.current_level_grade = {}
        self.areas_topics_help = []

        # Parent/guardian details
        self.parent_guardian_name = ""
        self.relationship_with_student = ""
        self.parent_mobile_number = ""
        self.parent_email_address = ""
        self.preferred_communication_method = ""

    def __str__(self):
        return (
            f"Student: {self.full_name} | Age: {self.age} | "
            f"School: {self.school_college_name} | "
            f"Grade: {self.class_grade}"
        )
 