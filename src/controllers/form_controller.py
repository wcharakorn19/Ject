from services.form_service import FormService


class FormController:
    def __init__(self):
        self.service = FormService()

    def get_form1_detail(self, submission_id: str):
        # 1. ไปเรียก Service ให้ยิง API
        data, error = self.service.fetch_form1_detail(submission_id)

        if error:
            return {"success": False, "message": error, "data": None}

        # 2. แกะกล่องข้อมูล
        detail = data.get("documentDetail", {})
        advisors_list = data.get("advisors", [])

        # ฟังก์ชันคำนวณชื่ออาจารย์
        def get_advisor_name(adv_id):
            if not adv_id:
                return "-"
            for adv in advisors_list:
                if adv.get("advisor_id") == adv_id:
                    return f"{adv.get('prefix_th')}{adv.get('first_name_th')} {adv.get('last_name_th')}"
            return f"รหัส {adv_id}"

        # 3. จัดเรียงข้อมูลให้เป็นระเบียบ เตรียมส่งให้ UI
        prefix = detail.get("prefix_th") or ""
        first = detail.get("first_name_th") or ""
        last = detail.get("last_name_th") or ""

        req_main_id = detail.get("form_details", {}).get(
            "main_advisor_id"
        ) or detail.get("main_advisor_id")
        req_co_id = detail.get("form_details", {}).get("co_advisor_id") or detail.get(
            "co_advisor_id"
        )

        formatted_data = {
            "student_name": f"{prefix}{first} {last}".strip() or "ไม่ระบุ",
            "student_id": detail.get("student_id", "-"),
            "degree": detail.get("degree", "-"),
            "program_name": detail.get("program_name", "-"),
            "department_name": detail.get("department_name", "-"),
            "faculty": detail.get("faculty", "-"),
            "plan": detail.get("plan", "-"),
            "phone": detail.get("phone", "-"),
            "email": detail.get("email", "-"),
            "main_advisor": get_advisor_name(req_main_id),
            "co_advisor": get_advisor_name(req_co_id),
        }

        return {"success": True, "data": formatted_data}

    def get_form2_detail(self, submission_id: str):
        # 1. ไปเรียก Service ให้ยิง API (ใช้ฟังก์ชันเดียวกับ Form 1 ได้เลยถ้าตั้งชื่อเป็น fetch_form_detail)
        # ถ้าของเดิมตั้งชื่อว่า fetch_form1_detail ก็แก้ให้เป็นชื่อกลางๆ หรือเรียกใช้ไปก่อนได้ครับ
        data, error = self.service.fetch_form1_detail(submission_id)

        if error:
            return {"success": False, "message": error, "data": None}

        # 2. แกะกล่องข้อมูล
        detail = data.get("documentDetail", {})
        advisors_list = data.get("advisors", [])

        # ฟังก์ชันคำนวณชื่ออาจารย์
        def get_advisor_name(adv_id):
            if not adv_id:
                return "-"
            for adv in advisors_list:
                if adv.get("advisor_id") == adv_id:
                    return f"{adv.get('prefix_th')}{adv.get('first_name_th')} {adv.get('last_name_th')}"
            return f"รหัส {adv_id}"

        # 3. จัดเรียงข้อมูลให้เป็นระเบียบ เตรียมส่งให้ UI
        prefix = detail.get("prefix_th") or ""
        first = detail.get("first_name_th") or ""
        last = detail.get("last_name_th") or ""

        form_details = detail.get("form_details", {})
        committee = form_details.get("committee", {})

        req_main_id = form_details.get("main_advisor_id") or detail.get(
            "main_advisor_id"
        )
        req_co_id = form_details.get("co_advisor_id") or detail.get("co_advisor1_id")

        # ปั้น Dictionary สวยๆ ส่งกลับไป
        formatted_data = {
            "student_name": f"{prefix}{first} {last}".strip() or "ไม่ระบุ",
            "student_id": detail.get("student_id", "-"),
            "degree": detail.get("degree", "-"),
            "program_name": detail.get("program_name", "-"),
            "department_name": detail.get("department_name", "-"),
            "main_advisor": get_advisor_name(req_main_id),
            "co_advisor": get_advisor_name(req_co_id),
            "chair": get_advisor_name(committee.get("chair_id")),
            "committee": get_advisor_name(committee.get("co_advisor2_id")),
            "member5": get_advisor_name(committee.get("member5_id")),
            "reserve_ext": get_advisor_name(committee.get("reserve_external_id")),
            "reserve_int": get_advisor_name(committee.get("reserve_internal_id")),
        }

        return {"success": True, "data": formatted_data}

    def get_form3_detail(self, submission_id: str):
        # ใช้ service ตัวเดิมดึง API จาก Postman Mock Server ได้เลย
        data, error = self.service.fetch_form1_detail(submission_id)

        if error:
            return {"success": False, "message": error, "data": None}

        detail = data.get("documentDetail", {})
        advisors_list = data.get("advisors", [])

        def get_advisor_name(adv_id):
            if not adv_id:
                return "-"
            for adv in advisors_list:
                if adv.get("advisor_id") == adv_id:
                    return f"{adv.get('prefix_th')}{adv.get('first_name_th')} {adv.get('last_name_th')}"
            return f"รหัส {adv_id}"

        prefix = detail.get("prefix_th") or ""
        first = detail.get("first_name_th") or ""
        last = detail.get("last_name_th") or ""

        form_details = detail.get("form_details", {})
        committee = form_details.get("committee", {})

        main_id = form_details.get("main_advisor_id") or detail.get("main_advisor_id")
        co_id = form_details.get("co_advisor_id") or detail.get("co_advisor1_id")

        formatted_data = {
            "student_name": f"{prefix}{first} {last}".strip() or "ไม่ระบุ",
            "student_id": detail.get("student_id", "-"),
            "degree": detail.get("degree", "-"),
            "program_name": detail.get("program_name", "-"),
            "department_name": detail.get("department_name", "-"),
            "approve_date": form_details.get("approved_date")
            or detail.get("updated_at", "-")[:10],
            "title_th": form_details.get("thesis_title_th", "-"),
            "title_en": form_details.get("thesis_title_en", "-"),
            "chair": get_advisor_name(committee.get("chair_id")),
            "main_advisor": get_advisor_name(main_id),
            "co_advisor": get_advisor_name(co_id),
        }

        return {"success": True, "data": formatted_data}

    def get_form4_detail(self, submission_id: str):
        # 1. ยิง API ไปขอข้อมูลจาก Service (ใช้ตัวเดิมได้เลย)
        data, error = self.service.fetch_form1_detail(submission_id)

        if error:
            return {"success": False, "message": error, "data": None}

        # 2. แกะกล่องข้อมูล JSON
        detail = data.get("documentDetail", {})
        form_details = detail.get("form_details", {})
        expert_info = form_details.get("expert_info", {})

        prefix = detail.get("prefix_th") or ""
        first = detail.get("first_name_th") or ""
        last = detail.get("last_name_th") or ""

        # 3. จัดแพ็กเกจข้อมูลให้ UI เอาไปใช้ง่ายๆ
        formatted_data = {
            "student_name": f"{prefix}{first} {last}".strip() or "ไม่ระบุ",
            "student_id": detail.get("student_id", "-"),
            "degree": detail.get("degree", "-"),
            "program_name": detail.get("program_name", "-"),
            "department_name": detail.get("department_name", "-"),
            "approve_date": form_details.get("approved_date", "-"),
            "title_th": form_details.get("thesis_title_th", "-"),
            "title_en": form_details.get("thesis_title_en", "-"),
            "expert_title": expert_info.get("title", "-"),
            "expert_name": expert_info.get("firstname", "-"),
            "expert_surname": expert_info.get("lastname", "-"),
            "expert_org": expert_info.get("institution", "-"),
            "expert_phone": expert_info.get("phone", "-"),
            "expert_email": expert_info.get("email", "-"),
        }

        return {"success": True, "data": formatted_data}

    def get_form5_detail(self, submission_id: str):
        # 1. ยิง API ขอข้อมูล
        data, error = self.service.fetch_form1_detail(submission_id)

        if error:
            return {"success": False, "message": error, "data": None}

        detail = data.get("documentDetail", {})
        form_details = detail.get("form_details", {})

        prefix = detail.get("prefix_th") or ""
        first = detail.get("first_name_th") or ""
        last = detail.get("last_name_th") or ""

        # 2. แกะข้อมูล Checkbox
        methods = form_details.get("collection_methods", [])
        methods_str = str(methods).lower()

        is_questionnaire = "questionnaire" in methods_str or "แบบสอบถาม" in methods_str
        is_test = "test" in methods_str or "แบบทดสอบ" in methods_str
        is_teaching = (
            "teaching" in methods_str
            or "experiment" in methods_str
            or "ทดลองสอน" in methods_str
        )
        is_other = "other" in methods_str or "อื่นๆ" in methods_str

        other_text = form_details.get("other_detail", "") if is_other else ""

        # 3. จัดแพ็กเกจส่งกลับ
        formatted_data = {
            "student_name": f"{prefix}{first} {last}".strip() or "ไม่ระบุ",
            "student_id": detail.get("student_id", "-"),
            "degree": detail.get("degree", "-"),
            "program_name": detail.get("program_name", "-"),
            "department_name": detail.get("department_name", "-"),
            "approve_date": form_details.get("approved_date", "-"),
            "title_th": form_details.get("thesis_title_th", "-"),
            "title_en": form_details.get("thesis_title_en", "-"),
            # โยนค่า True/False ไปให้ UI ใช้เลย
            "check_questionnaire": is_questionnaire,
            "check_test": is_test,
            "check_teaching": is_teaching,
            "check_other": is_other,
            "other_detail": other_text,
        }

        return {"success": True, "data": formatted_data}

    def get_form6_detail(self, submission_id: str):
        # 1. ยิง API ขอข้อมูลจาก Postman
        data, error = self.service.fetch_form1_detail(submission_id)

        if error:
            return {"success": False, "message": error, "data": None}

        detail = data.get("documentDetail", {})
        advisors_list = data.get("advisors", [])  # ดึงรายชื่ออาจารย์จาก Postman มาเทียบ
        form_details = detail.get("form_details", {})
        committee = form_details.get("committee", {})

        # ฟังก์ชันค้นหาชื่ออาจารย์
        def get_advisor_name(adv_id):
            if not adv_id:
                return "-"
            for adv in advisors_list:
                if adv.get("advisor_id") == adv_id:
                    return f"{adv.get('prefix_th')}{adv.get('first_name_th')} {adv.get('last_name_th')}"
            return f"รหัส {adv_id}"

        prefix = detail.get("prefix_th") or ""
        first = detail.get("first_name_th") or ""
        last = detail.get("last_name_th") or ""

        formatted_data = {
            "student_name": f"{prefix}{first} {last}".strip() or "ไม่ระบุ",
            "student_id": detail.get("student_id", "-"),
            "degree": detail.get("degree", "-"),
            "program_name": detail.get("program_name", "-"),
            "department_name": detail.get("department_name", "-"),
            "phone": detail.get("phone", "-"),
            "start_semester": str(form_details.get("entry_semester", "-")),
            "start_year": str(form_details.get("entry_year", "-")),
            "address": form_details.get("current_address", "-"),
            "workplace": form_details.get("workplace", "-"),
            "thesis_th": form_details.get("thesis_title_th", "-"),
            "thesis_en": form_details.get("thesis_title_en", "-"),
            "main_advisor": get_advisor_name(form_details.get("main_advisor_id")),
            "co_advisor": get_advisor_name(form_details.get("co_advisor_id")),
            "chair": get_advisor_name(committee.get("chair_id")),
            "committee": get_advisor_name(committee.get("co_advisor2_id")),
            "member5": get_advisor_name(committee.get("member5_id")),
            "reserve_ext": get_advisor_name(committee.get("reserve_external_id")),
            "reserve_int": get_advisor_name(committee.get("reserve_internal_id")),
        }

        return {"success": True, "data": formatted_data}

    # 🌟 ฟังก์ชันดึงข้อมูล Exam Result (ฟอร์มสุดท้ายแล้วเว้ย!)
    def get_exam_result_detail(self, submission_id: str):
        # 1. ยิง API ขอข้อมูล
        data, error = self.service.fetch_form1_detail(submission_id)

        if error:
            return {"success": False, "message": error, "data": None}

        detail = data.get("documentDetail", {})
        form_details = detail.get("form_details", {})

        prefix = detail.get("prefix_th") or ""
        first = detail.get("first_name_th") or ""
        last = detail.get("last_name_th") or ""

        # เช็คว่าใช้คีย์ result หรือ total_score
        score = (
            form_details.get("result")
            if "result" in form_details
            else form_details.get("total_score", "-")
        )

        formatted_data = {
            "student_name": f"{prefix}{first} {last}".strip() or "ไม่ระบุ",
            "student_id": detail.get("student_id", "-"),
            "degree": detail.get("degree", "-"),
            "program_name": detail.get("program_name", "-"),
            "doc_type": detail.get("title", "แบบฟอร์มยื่นผลการสอบ"),
            "exam_type": form_details.get("exam_type", "-"),
            "exam_date": form_details.get("exam_date", "-"),
            "result_score": str(score),
            # ส่งลิสต์ไฟล์ไปให้ UI วนลูปสร้างปุ่ม
            "files": form_details.get("files", []),
        }

        return {"success": True, "data": formatted_data}
