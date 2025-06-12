from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Home page to list links to different forms
    return render_template('home.html')

@app.route('/area1/sub1')
def area1_sub1():
    return "<h1>Area 1 - Sub Area 1</h1>"

@app.route('/area1/sub2')
def area1_sub2():
    return "<h1>Area 1 - Sub Area 2</h1>"

@app.route('/area1/sub3')
def area1_sub3():
    return "<h1>Area 1 - Sub Area 3</h1>"

# 添加 Area 2 和 Area 3 的路由
@app.route('/area2/sub1')
def area2_sub1():
    return "<h1>Area 2 - Sub Area 1</h1>"

@app.route('/area3/sub3')
def area3_sub3():
    return "<h1>Area 3 - Sub Area 3</h1>"


@app.route('/form1', methods=['GET', 'POST'])
def form1():
    if request.method == 'POST':
        # Process form1 data
        name = request.form['name']
        email = request.form['email']
        return f"Form 1 Submitted! Name: {name}, Email: {email}"
    return render_template('form.html')


@app.route('/form-config', methods=['GET'])
def form_config():
    # 动态字段配置，包括全局标签位置
    response = {
        'title': 'Grant Application',
        "label_position": "top",  # 全局标签位置，可以是 "top" 或 "left"
        # "label_position": "left",  # 全局标签位置，可以是 "top" 或 "left"
        # "allowManualInput": False,
        "allowManualInput": True,
        "fields": [
            {"name": "first_name", "label": "First Name", "type": "string", "required": True, "row": 1, "col": 3},
            {"name": "last_name", "label": "Last Name", "type": "string", "required": True, "row": 1, "col": 3},
            {"name": "email", "label": "Email", "type": "email", "required": True, "row": 2, "col": 6},
            {"name": "dob", "label": "Date of Birth", "type": "date", "required": True, "row": 2, "col": 6},
            {"name": "gender", "label": "Gender", "type": "radio", "options": ["Male", "Female"], "required": True, "row": 3},
            {"name": "subscribe", "label": "Subscribe to Newsletter", "type": "checkbox", "required": False, "row": 4}
        ]
    }
    return jsonify(response)

@app.route('/form-config-group', methods=['GET'])
def form_config_group():
    response = {
        'title': 'Grant Application',
        "label_position": "top",
        "allowManualInput": True,
        "groups": [
            {
                "name": "Basic Information",
                "fields": [
                    {"name": "first_name", "label": "First Name", "type": "string", "required": True, "col": 6},
                    {"name": "last_name", "label": "Last Name", "type": "string", "required": True, "col": 6},
                    {"name": "email", "label": "Email", "type": "email", "required": True, "col": 6},
                    {"name": "dob", "label": "Date of Birth", "type": "date", "required": True, "col": 6},
                ]
            },
            {
                "name": "Educational Background",
                "repeatable": True,
                "fields": [
                    {"name": "university", "label": "University", "type": "string", "required": True, "col": 4},
                    {"name": "degree", "label": "Degree", "type": "string", "required": True, "col": 4},
                    {"name": "graduation_date", "label": "Graduation Date", "type": "date", "required": True, "col": 4},
                ]
            },
            {
                "name": "Research Information",
                "fields": [
                    {"name": "research_topic", "label": "Research Topic", "type": "string", "required": True, "col": 12},
                    {"name": "publications", "label": "Publications", "type": "string", "required": False, "col": 12},
                ]
            },
        ]
    }
   
    return jsonify(response)



@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        # Process form2 data
        category = request.form['category']
        feedback = request.form['feedback']
        return f"Form 2 Submitted! Category: {category}, Feedback: {feedback}"
    return render_template('form2.html')


@app.route('/academic-research/job-application', methods=['GET', 'POST'])
def job_application_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('A11.html', data)
        return jsonify({
            "message": "Application Submitted Successfully!",
            "data": data
        })
    return render_template('A11.html')

@app.route('/academic-research/grant-application', methods=['GET', 'POST'])
def grant_application_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('A12.html', data)
        return jsonify({
            "message": "Application Submitted Successfully!",
            "data": data
        })
    return render_template('A12.html')

@app.route('/academic-research/student-registration', methods=['GET', 'POST'])
def student_registration():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('A13.html', data)
        return jsonify({
            "message": "Student Registration Submitted Successfully!",
            "data": data
        })
    return render_template('A13.html')

@app.route('/academic-research/paper-submission', methods=['GET', 'POST'])
def paper_submission():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('A14.html', data)
        return jsonify({
            "message": "Paper Submission Successful!",
            "data": data
        })
    return render_template('A14.html')

@app.route('/academic-research/course-registration', methods=['GET', 'POST'])
def course_registration():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('A15.html', data)
        return jsonify({
            "message": "Course Registration Successful!",
            "data": data
        })
    return render_template('A15.html')

@app.route('/academic-research/scholarship-application', methods=['GET', 'POST'])
def scholarship_application():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('A13.html', data)
        return jsonify({
            "message": "Scholarship Application Submitted Successfully!",
            "data": data
        })
    return render_template('A13.html')

@app.route('/professional-business/startup-funding', methods=['GET', 'POST'])
def startup_funding():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('B11.html', data)
        return jsonify({
            "message": "Startup Funding Application Submitted Successfully!",
            "data": data
        })
    return render_template('B11.html')

@app.route('/professional-business/rental-application', methods=['GET', 'POST'])
def rental_application():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('B12.html', data)
        return jsonify({
            "message": "Real Estate Rental Application Submitted Successfully!",
            "data": data
        })
    return render_template('B12.html')

@app.route('/professional-business/workshop-registration', methods=['GET', 'POST'])
def workshop_registration():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('B13.html', data)
        return jsonify({
            "message": "Workshop Registration Submitted Successfully!",
            "data": data
        })
    return render_template('B13.html')

@app.route('/professional-business/membership-application', methods=['GET', 'POST'])
def membership_application():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('B14.html', data)
        return jsonify({
            "message": "Membership Application Submitted Successfully!",
            "data": data
        })
    return render_template('B14.html')

@app.route('/arts-creative/exhibition-submission', methods=['GET', 'POST'])
def exhibition_submission():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('C11.html', data)
        return jsonify({
            "message": "Art Exhibition Submission Successful!",
            "data": data
        })
    return render_template('C11.html')

@app.route('/arts-creative/literary-submission', methods=['GET', 'POST'])
def literary_submission():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('C12.html', data)
        return jsonify({
            "message": "Literary Work Submission Successful!",
            "data": data
        })
    return render_template('C12.html')

@app.route('/arts-creative/speaker-application', methods=['GET', 'POST'])
def speaker_application():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('C13.html', data)
        return jsonify({
            "message": "Speaker Application Submitted Successfully!",
            "data": data
        })
    return render_template('C13.html')

@app.route('/tech-software/bug-report', methods=['GET', 'POST'])
def bug_report():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('D11.html', data)
        return jsonify({
            "message": "Bug Report Submitted Successfully!",
            "data": data
        })
    return render_template('D11.html')

@app.route('/tech-software/support-request', methods=['GET', 'POST'])
def support_request():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('D12.html', data)
        return jsonify({
            "message": "IT Support Request Submitted Successfully!",
            "data": data
        })
    return render_template('D12.html')

@app.route('/finance-banking/personal-loan', methods=['GET', 'POST'])
def personal_loan():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('E11.html', data)
        return jsonify({
            "message": "Personal Loan Application Submitted Successfully!",
            "data": data
        })
    return render_template('E11.html')

@app.route('/finance-banking/account-opening', methods=['GET', 'POST'])
def account_opening():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('E12.html', data)
        return jsonify({
            "message": "Account Opening Application Submitted Successfully!",
            "data": data
        })
    return render_template('E12.html')

@app.route('/finance-banking/financial-planning', methods=['GET', 'POST'])
def financial_planning():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('E13.html', data)
        return jsonify({
            "message": "Financial Planning Consultation Request Submitted Successfully!",
            "data": data
        })
    return render_template('E13.html')

@app.route('/healthcare-medical/patient-consent', methods=['GET', 'POST'])
def patient_consent():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('F11.html', data)
        return jsonify({
            "message": "Patient Consent Form Submitted Successfully!",
            "data": data
        })
    return render_template('F11.html')

@app.route('/healthcare-medical/research-enrollment', methods=['GET', 'POST'])
def research_enrollment():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('F12.html', data)
        return jsonify({
            "message": "Research Study Enrollment Submitted Successfully!",
            "data": data
        })
    return render_template('F12.html')

@app.route('/healthcare-medical/insurance-claim', methods=['GET', 'POST'])
def insurance_claim():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('F13.html', data)
        return jsonify({
            "message": "Insurance Claim Form Submitted Successfully!",
            "data": data
        })
    return render_template('F13.html')

@app.route('/legal-compliance/nda-submission', methods=['GET', 'POST'])
def nda_submission():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('G11.html', data)
        return jsonify({
            "message": "NDA Submitted Successfully!",
            "data": data
        })
    return render_template('G11.html')

@app.route('/legal-compliance/background-check', methods=['GET', 'POST'])
def background_check():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('G12.html', data)
        return jsonify({
            "message": "Background Check Authorization Submitted Successfully!",
            "data": data
        })
    return render_template('G12.html')

@app.route('/legal-compliance/contractor-onboarding', methods=['GET', 'POST'])
def contractor_onboarding():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('G13.html', data)
        return jsonify({
            "message": "Contractor Onboarding Form Submitted Successfully!",
            "data": data
        })
    return render_template('G13.html')

@app.route('/construction-manufacturing/project-bid', methods=['GET', 'POST'])
def project_bid():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('H11.html', data)
        return jsonify({
            "message": "Project Bid Submitted Successfully!",
            "data": data
        })
    return render_template('H11.html')

@app.route('/construction-manufacturing/order-request', methods=['GET', 'POST'])
def order_request():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_submission_to_json('H12.html', data)
        return jsonify({
            "message": "Manufacturing Order Request Submitted Successfully!",
            "data": data
        })
    return render_template('H12.html')

# 添加辅助函数
def save_submission_to_json(template_name, data):
    """将提交的数据保存到对应的JSON文件中"""
    # 确保submission文件夹存在
    if not os.path.exists('submission'):
        os.makedirs('submission')
    
    # 构建JSON文件路径
    filename = f"submission/{template_name.replace('.html', '')}.json"
    
    # 添加时间戳
    data['submission_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 读取现有数据或创建新的数据列表
    submissions = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            submissions = json.load(f)
    
    # 添加新提交的数据
    submissions.append(data)
    
    # 保存更新后的数据
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(submissions, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
