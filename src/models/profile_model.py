from dataclasses import dataclass, field


@dataclass
class ThesisModel:
    title_th: str = "-"
    title_en: str = "-"
    main_advisor: str = "-"
    co_advisor_1: str = "-"
    co_advisor_2: str = "-"


@dataclass
class ProgressModel:
    topic_exam_date: str = "-"
    topic_status: str = "-"
    topic_approve_date: str = "-"
    final_exam_date: str = "-"
    final_status: str = "-"
    final_approve_date: str = "-"
    english_test_type: str = "-"
    english_test_date: str = "-"
    english_test_status: str = "-"


@dataclass
class ProfileModel:
    user_id: str = "-"
    full_name: str = "-"
    role: str = "-"
    email: str = "-"
    phone: str = "-"
    education_level: str = "-"
    faculty: str = "-"
    major: str = "-"
    status: str = "-"
    thesis: ThesisModel = field(default_factory=ThesisModel)
    progress: ProgressModel = field(default_factory=ProgressModel)
