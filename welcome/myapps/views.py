from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .forms import StudentLoginForm
from .models import CollegeStudent
from django.contrib import messages
from .models import GroupMessage
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import GroupMessage
from .models import Result
from .models import Assignment
from .models import Certificate
import pandas as pd
import os
from django.conf import settings
import pandas as pd
import os
from django.conf import settings

# Example login view
from django.contrib import messages

from django.contrib import messages

def login_view(request):

    # ✅ GET ROLE FROM SELECTION PAGE
    role = request.GET.get("role")
    if role:
        request.session['role'] = role

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        current_role = request.session.get("role")

        # OFFICE LOGIN (keep as it is)
        if username == "office" and password == "ace123":
            return redirect('office_dashboard')

        # ✅ STUDENT USERS
        student_users = {
            "Aarav Sharma V": "6176AC22UCS01",
            "Aadhya Iyer S": "6176AC22UCS02",
            "Arjun Kumar M": "6176AC22UCS03",
            "Ananya Reddy S": "6176AC22UCS04",
            "Rahul Verma T": "6176AC22UCS05",
            "Sneha Nair Y": "6176AC22UCS06",
            "Karthik Raj R": "6176AC22UCS07",
            "Meera Krishnan P": "6176AC22UCS08",
            "Rohit Singh M": "6176AC22UCS09",
            "Priya Menon S": "6176AC22UCS010",
            "Vivek Patel T": "6176AC22UCS011",
            "Divya Sharma S": "6176AC22UCS012",
            "Aditya Gupta D": "6176AC22UCS013",
            "Kavya Srinivasan G": "6176AC22UCS014",
            "Suresh Babu S": "6176AC22UCS015",
            "Neha Agarwal C": "6176AC22UCS016",
            "Varun Shetty A": "6176AC22UCS017",
            "Pooja Desai M": "6176AC22UCS018",
            "Nikhil Jain N": "6176AC22UCS019",
            "Lakshmi Narayanan P": "6176AC22UCS020",
            "Manish Yadav B": "6176AC22UCS021",
            "Swathi Ramesh D": "6176AC22UCS022",
            "Deepak Mishra K": "6176AC22UCS023",
            "Riya Kapoor L": "6176AC22UCS024",
            "Sanjay Das A": "6176AC22UCS025",
            "Harini Subramanian C": "6176AC22UCS026",
            "Akash Mehta V": "6176AC22UCS027",
            "Shalini Gupta B": "6176AC22UCS028",
            "Gokul Krishna A": "6176AC22UCS029",
            "Tanvi Joshi H": "6176AC22UCS030",
            "Aravindhan K": "6176AC22UCS031",
            "Karthikeyan J": "6176AC22UCS032",
            "Praveen Kumar T": "6176AC22UCS033",
            "Dinesh Kumar A": "6176AC22UCS034",
            "Vigneshwaran B": "6176AC22UCS035",
            "Suresh Kumar G": "6176AC22UCS036",
            "Gopinath M": "6176AC22UCS037",
            "Saravanan O": "6176AC22UCS038",
            "Ramesh Kumar P": "6176AC22UCS039",
            "Elangovan S": "6176AC22UCS040",
            "Balasubramanian C": "6176AC22UCS041",
            "Manikandan K": "6176AC22UCS042",
            "Senthil Kumar D": "6176AC22UCS043",
            "Muthukumar E": "6176AC22UCS044",
            "Chandrasekar S": "6176AC22UCS045",
            "Rajasekar A": "6176AC22UCS046",
            "Thirunavukarasu L": "6176AC22UCS047",
            "Kannan N": "6176AC22UCS048",
            "Murugan S": "6176AC22UCS049",
            "Periyasamy G": "6176AC22UCS050",
            "Selvakumar V": "6176AC22UCS051",
            "Pandian M": "6176AC22UCS052",
            "Ganesan N": "6176AC22UCS053",
            "Karthi L": "6176AC22UCS054",
            "Velmurugan C": "6176AC22UCS055",
            "Marimuthu S": "6176AC22UCS056",
            "Shanmugam A": "6176AC22UCS057",
            "Natarajan R": "6176AC22UCS058",
            "Ilayaraja D": "6176AC22UCS059",
            "Thangavel M": "6176AC22UCS060",
            "Arun Kumar L": "6176AC22UCS061",
            "Prasanna M": "6176AC22UCS062",
            "Naveen Kumar S": "6176AC22UCS063",
            "Yuvaraj P": "6176AC22UCS064",
            "Sakthivel T": "6176AC22UCS065",
            "Bharath Kumar S": "6176AC22UCS066",
            "Karthick P": "6176AC22UCS067",
            "Vinoth Kumar A": "6176AC22UCS068",
            "Prabhu S": "6176AC22UCS069",
            "Jegan D": "6176AC22UCS070",
            "Lenin P": "6176AC22UCS071",
            "Sakthikumar A": "6176AC22UCS072",
            "Ashwin Kumar G": "6176AC22UCS073",
            "Kishore Kumar T": "6176AC22UCS074",
            "Siva Kumar B": "6176AC22UCS075",
            "Dhanush R": "6176AC22UCS076",
            "Madhan S": "6176AC22UCS077",
            "Sathish Kumar R": "6176AC22UCS078",
            "Rajkumar M": "6176AC22UCS079",
            "Hariharan S": "6176AC22UCS080",
            "Raghavan N": "6176AC22UCS081",
            "Gokulan S": "6176AC22UCS082",
            "Sudhakar B": "6176AC22UCS083",
            "Guru prasath K": "6176AC22UCS084",
            "Parthiban V": "6176AC22UCS085",
            "Anbazhagan C": "6176AC22UCS086",
            "Tamilarasan T": "6176AC22UCS087",
            "Prakash S": "6176AC22UCS088",
            "Devaraj D": "6176AC22UCS089",
            "Boopathi P": "6176AC22UCS090",
        }

        # ✅ STAFF USERS
        staff_users = {
            "Xavier Mary": "mary123",
            "Vinoth Kumar": "vinoth123",
            "Dhanalakshmi": "dhana123",
            "Vikram": "vikram123",
            "Meena": "meena123"
        }

        # 🎓 STUDENT LOGIN (ONLY if role = student)
        if current_role == "student":
            if username in student_users and student_users[username] == password:
                request.session['student_name'] = username
                request.session['student_reg'] = password
                return redirect('student_dashboard')
            else:
                messages.error(request, "Invalid Student Login")

        # 👨‍🏫 STAFF LOGIN (ONLY if role = staff)
        elif current_role == "staff":
            if username in staff_users and staff_users[username] == password:
                request.session['user'] = username
                return redirect('staff_classes')
            else:
                messages.error(request, "Invalid Staff Login")

        # 👤 VISITOR LOGIN
        elif current_role == "visitor":
            request.session['visitor'] = True
            return redirect('chat')

        # ❌ FALLBACK
        else:
            messages.error(request, "Invalid Access")

    return render(request, "login.html")
# Chat view
def chat_view(request):
    if request.method == "POST":
        question = request.POST.get("question").strip()
        # Basic bot logic for location answers
        location_keywords = {
            "adhiyamaan college of engineering": "The ADHIYAMAAN COLLEGE OF ENGINEERING is located at Dr.M.G.R. Nagar,HOSUR.",
            "library": "The LIBRARY is Behind the main block.",
            "canteen": "The CANTEEN is behind the main block right side to the Library.",
            "cse department": "The CSE DEPARTMENT is in the main block first floor.",
            "ece department": "The ECE DEPARTMENT is in the main block second floor.",
            "eee department": "The EEE DEPARTMENT is in the main block third floor.",
            "chemical department": "The CHEMICAL DEPARTMENT is in the architecture block first floor.",
            "it department": "The IT DEPARTMENT is in the main block second floor.",
            "biotech department": "The BIOTECH DEPARTMENT is in the architecture block first floor.",
            "aeronotical department": "The AERONOTICAL DEPARTMENT is in the main block ground floor.",
            "mechanical department": "The MECHANICAL DEPARTMENT is behind the library.",
            "mca block": "The MCA BLOCK is in the main block second floor.",
            "mba block": "The MBA BLOCK is inside the library block ground floor.",
            "me block": "The ME BLOCK is inside the Main block first floor.",
            "office room": "The OFFICE ROOM is opposite to the canteen first floor.",
            "placement cell": "The PLACEMENT CELL is inside the main block in ground floor.",
            "room number 114": "THE ROOM NUMBER 114 is inside the main block first floor ",
            "cse hod room": "The cse hod room is inside the main block first floor ",
            "seminar hall":"Seminar Hall is in main building first floor near lab 2"

        }

        is_location = False
        bot_response = "I am not sure about that."

        for key, answer in location_keywords.items():
            if key in question.lower():
                bot_response = answer
                is_location = True
                break

        # Initialize chat_history in session
        if 'chat_history' not in request.session:
            request.session['chat_history'] = []

        request.session['chat_history'].append({
            'user': question,
            'bot': bot_response,
            'is_location': is_location
        })
        request.session.modified = True

    chat_history = request.session.get('chat_history', [])
    return render(request, "chat.html", {'chat_history': chat_history})


# Map view
def map_view(request):
    return render(request, "map.html")


# Logout view
def logout_view(request):
    request.session.flush()
    return redirect('login')

# Staff login
def staff_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # simple login check
        if username == "staff" and password == "1234":
            return redirect('staff_chat')

    return render(request, "staff_login.html")


# Staff chat page

from django.shortcuts import render, redirect
from .models import GroupMessage


from django.shortcuts import render, redirect
from .models import GroupMessage


def staff_chat(request):

    groups = [
        "CSE STUDENTS",
        "FIRST YEAR CSE",
        "SECOND YEAR CSE",
        "THIRD YEAR CSE",
        "FINAL YEAR CSE",
    ]

    selected_group = request.GET.get("group")

    messages = []

    if selected_group:
        messages = GroupMessage.objects.filter(
            group_name=selected_group
        ).order_by("time")

    if request.method == "POST":

        group = request.POST.get("group")
        text = request.POST.get("message")

        if text:
            GroupMessage.objects.create(
                group_name=group,
                sender="Staff",
                message=text
            )

        return redirect(f"/staff-chat/?group={group}")

    return render(request, "staff_chat.html", {
        "groups": groups,
        "messages": messages,
        "selected_group": selected_group
    })
def delete_message(request, group_name, msg_index):

    session_key = f"chat_{group_name}"

    messages = request.session.get(session_key, [])

    if 0 <= msg_index < len(messages):
        messages.pop(msg_index)

    request.session[session_key] = messages
    request.session.modified = True

    return redirect('group_chat', group_name=group_name)
def share_message(request, group_name, msg_index):

    groups = [
        "CSE STUDENTS",
        "FIRST YEAR CSE A",
        "FIRST YEAR CSE B",
        "SECOND YEAR CSE"
    ]

    session_key = f"chat_{group_name}"
    messages = request.session.get(session_key, [])

    if msg_index >= len(messages):
        return redirect("group_chat", group_name=group_name)

    message = messages[msg_index]

    if request.method == "POST":

        selected_groups = request.POST.getlist("groups")
        for g in selected_groups:
            key = f"chat_{g}"
            group_msgs = request.session.get(key, [])

            group_msgs.append(message)

            request.session[key] = group_msgs

        request.session.modified = True

        return redirect("staff_chat")

    return render(request, "share_message.html", {
        "groups": groups,
        "message": message
    })
def student_login(request):
    if request.method == "POST":

        name = request.POST.get("name")
        reg_no = request.POST.get("reg_no")

        # Check reg number starts with 6176AC
        if reg_no.startswith("6176AC"):

            # Save student info in session
            request.session['student_name'] = name
            request.session['student_reg'] = reg_no

            return redirect('student_dashboard')

        else:
            messages.error(request, "Invalid Register Number")

    return render(request, "student_login.html")






def student_dashboard(request):
    if 'student_name' not in request.session:
            return redirect('login')

    from .models import NoDueVerification

    # get logged-in student register number
    register_number = request.session.get("register_number")

    # get ONLY this student's verification
    verification = NoDueVerification.objects.filter(
        register_number=register_number
    ).first()

    return render(request, 'student_dashboard.html', {
        "verification": verification
    })

from django.shortcuts import render, redirect
from .models import GroupMessage


def student_chat(request):

    groups = [
        "CSE STUDENTS",
        "FIRST YEAR CSE",
        "SECOND YEAR CSE",
        "THIRD YEAR CSE",
        "FINAL YEAR CSE",
    ]

    # Get selected group from URL
    group = request.GET.get("group")

    messages = []

    if group:
        messages = GroupMessage.objects.filter(
            group_name=group
        ).order_by("time")

    # Get student login name
    username = request.session.get("student_name", "Student")

    # When student sends message
    if request.method == "POST":

        group = request.POST.get("group")
        message = request.POST.get("message")

        if group and message:
            GroupMessage.objects.create(
                group_name=group,
                sender=username,
                message=message
            )

        return redirect(f"/student-chat/?group={group}")

    return render(request, "student_chat.html", {
        "groups": groups,
        "messages": messages,
        "group": group,
        "username": username
    })

def delete_student_message(request, index):

    messages = request.session.get('chat_messages', [])

    if 0 <= index < len(messages):
        messages.pop(index)

    request.session['chat_messages'] = messages

    return redirect('student_chat')
def group_chat(request, group_name):

    from .models import GroupMessage

    messages = GroupMessage.objects.filter(
        group_name=group_name
    ).order_by("time")

    if request.method == "POST":

        text = request.POST.get("message")

        if text:
            GroupMessage.objects.create(
                group_name=group_name,
                sender="Staff",
                message=text
            )

        return redirect("group_chat", group_name=group_name)

    return render(request, "group_chat.html", {
        "group_name": group_name,
        "messages": messages
    })
from django.shortcuts import render, redirect
from .models import GroupMessage

from django.shortcuts import render, redirect
from .models import GroupMessage


def student_chat(request):

    groups = [
        "CSE STUDENTS",
        "FIRST YEAR CSE",
        "SECOND YEAR CSE",
        "THIRD YEAR CSE",
        "FINAL YEAR CSE",
    ]

    group = request.GET.get("group")

    messages = []

    if group:
        messages = GroupMessage.objects.filter(group_name=group).order_by("time")

    username = request.session.get("student_name", "Student")

    if request.method == "POST":

        group = request.POST.get("group")
        text = request.POST.get("message")

        if text:
            GroupMessage.objects.create(
                group_name=group,
                sender=username,
                message=text
            )

        return redirect(f"/student-chat/?group={group}")

    return render(request, "student_chat.html", {
        "groups": groups,
        "messages": messages,
        "group": group
    })


def student_chat_groups(request):

    groups = [
        "CSE STUDENTS",
        "FIRST YEAR CSE",
        "SECOND YEAR CSE",
        "THIRD YEAR CSE",
        "FINAL YEAR CSE",
    ]

    return render(request, "student_chat.html", {"groups": groups})


def student_group_chat(request, group_name):

    messages = GroupMessage.objects.filter(
        group_name=group_name
    ).order_by("time")

    username = request.session.get("student_name", "Student")

    if request.method == "POST":

        text = request.POST.get("message")

        if text:
            GroupMessage.objects.create(
                group_name=group_name,
                sender=username,
                message=text
            )

        return redirect("student_group_chat", group_name=group_name)

    return render(request, "student_group_chat.html", {
        "messages": messages,
        "group_name": group_name
    })

def delete_message(request, id):
    msg = GroupMessage.objects.get(id=id)
    msg.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def student_result(request):

    results = Result.objects.all()

    return render(request,"student_result.html",{"results":results})

def feedback(request):

    from .models import Feedback

    if request.method == "POST":

        student_name = request.POST.get("username")
        reg = request.POST.get("registerno")

        staffs = [
            "Kalaivani",
            "Vinoth Kumar",
            "Dhanalakshmi",
            "Xavier Mary",
            "Vikram",
            "Meena"
        ]

        for i, staff in enumerate(staffs):

            Feedback.objects.create(
                student_name=student_name,
                register_number=reg,
                staff_name=staff,

                q1=request.POST.get(f"{i}_q1"),
                q2=request.POST.get(f"{i}_q2"),
                q3=request.POST.get(f"{i}_q3"),
                q4=request.POST.get(f"{i}_q4"),
                q5=request.POST.get(f"{i}_q5"),
                q6=request.POST.get(f"{i}_q6"),
                q7=request.POST.get(f"{i}_q7"),
                q8=request.POST.get(f"{i}_q8"),
                q9=request.POST.get(f"{i}_q9"),
                q10=request.POST.get(f"{i}_q10"),
            )

        return redirect("student_dashboard")

    return render(request, "feedback.html")
def timetable(request):
    return render(request,"timetable.html")


def cse_a(request):
    return render(request,"cse_a_timetable.html")


def cse_b(request):
    return render(request,"cse_b_timetable.html")


def cse_c(request):
    return render(request,"cse_c_timetable.html")

def assignment_upload(request):

    if request.method == "POST":

        student_name = request.POST.get("student_name")
        register_number = request.POST.get("register_number").strip().upper()
        year = request.POST.get("year")
        subject = request.POST.get("subject")
        assignment_no = request.POST.get("assignment_no")

        # Extract only number (1,2,3,4)
        assignment_no = ''.join(filter(str.isdigit, assignment_no))

        if assignment_no:
            assignment_no = int(assignment_no)
        else:
            assignment_no = None
        date = request.POST.get("date")
        file = request.FILES.get("assignment_file")
        section = request.POST.get("section")

        if file:

            Assignment.objects.create(
                student_name=student_name,
                register_number=register_number,
                year=year,
                subject=subject,
                assignment_no=assignment_no,
                date=date,
                assignment_file=file,
                section=section
            )

            return redirect("assignment_history")
    return render(request, "assignment_upload.html")

def assignment_history(request):

    assignments = Assignment.objects.all().order_by("-id")

    return render(request,"assignment_history.html",{"assignments":assignments})

def certificate_upload(request):

    if request.method == "POST":

        student_name = request.POST.get("student_name")
        register_number = request.POST.get("register_number")
        year = request.POST.get("year")
        date = request.POST.get("date")
        organization = request.POST.get("organization")
        file = request.FILES.get("certificate_file")

        if student_name and register_number and year and date and organization and file:

            Certificate.objects.create(
                student_name=student_name,
                register_number=register_number,
                year=year,
                date=date,
                organization=organization,
                certificate_file=file
            )

            return redirect("certificate_history")

    return render(request,"certificate_upload.html")
def staff_certificates(request):

    # show only first 30 certificates
    certificates = Certificate.objects.all().order_by("-id")[:30]

    return render(request, "staff_certificates.html", {
        "certificates": certificates
    })

def certificate_history(request):

    certificates = Certificate.objects.all().order_by("-id")

    return render(request,"certificate_history.html",{"certificates":certificates})

def no_due_form(request):
    return render(request,"no_due_form.html")

from .models import NoDueVerification

def no_due_table(request):
    from .models import NoDueVerification

    # get logged-in student register number
    register_number = request.session.get("student_reg")

    # filter only this student's data
    verifications = NoDueVerification.objects.filter(
        register_number=register_number
    )

    return render(request, "no_due_table.html", {
        "verifications": verifications
    })

def student_profile(request):

    return render(request,"student_profile.html")

def student_profile_table(request):
    from .models import StudentProfileVerification

    reg = request.session.get("student_reg")  # 🔥 important

    verifications = StudentProfileVerification.objects.filter(
        register_number=reg
    )

    return render(request, "student_profile_table.html", {
        "verifications": verifications
    })

def logout(request):
    return redirect("login")

def office(request):
    messages = GroupMessage.objects.all().order_by("time")

    return render(request, "office.html", {"messages": messages})

from django.shortcuts import render, redirect

def office_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "office" and password == "ace123":

            # ✅ VERY IMPORTANT LINE
            request.session.clear()   # 🔥 clears ALL old session

            # ✅ SET OFFICE LOGIN
            request.session['is_office'] = True

            return redirect('office_dashboard')

    return render(request, "office_login.html")

def office_chat(request):

    group = "OFFICE"   # 🔥 COMMON GROUP

    if request.method == "POST":

        message = request.POST.get("message")
        file = request.FILES.get("file")

        # ✅ SAVE BOTH MESSAGE + FILE IN SAME ROW
        if message or file:
            GroupMessage.objects.create(
                group_name=group,
                sender="Office",
                message=message if message else "",
                file=file
            )

        return redirect("office_chat")

    # ✅ FILTER ONLY OFFICE CHAT
    messages = GroupMessage.objects.filter(
        group_name=group
    ).order_by("time")

    return render(request, "office_chat.html", {"messages": messages})
def staff_classes(request):
    return render(request, "staff_classes.html")

def staff_dashboard(request):
    return render(request, "staff_dashboard.html")

def staff_certificates(request):
    certificates = Certificate.objects.all().order_by("-id")
    return render(request, "staff_certificates.html", {"certificates": certificates})
from django.shortcuts import render
from .models import Assignment

import pandas as pd
import os
from django.conf import settings
from .models import Assignment

from .models import Assignment
from .models import Assignment

def staff_assignments(request, section):

    import pandas as pd
    import os
    from django.conf import settings
    from .models import Assignment

    # ✅ LOAD EXCEL BASED ON SECTION
    if section == "A":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_a.xlsx")
    elif section == "B":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_b.xlsx")
    else:
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_c.xlsx")

    df = pd.read_excel(file_path)

    # ✅ CLEAN COLUMN NAMES
    df.columns = df.columns.str.strip().str.upper()

    students_excel = df.to_dict(orient="records")

    # ✅ GET ALL ASSIGNMENTS FROM DB
    assignments = Assignment.objects.filter(section=section)
    current_staff = request.session.get("user")

    staff_subject_map = {
        "Vikram": ["bda", "big data"],
        "Xavier Mary": ["ai", "artificial intelligence"],
        "Vinoth Kumar": ["ml", "machine learning"],
        "Dhanalakshmi": ["cc", "cloud computing"],
        "Meena": ["cyber security", "cs"]
    }

    # ✅ FILTER BASED ON STAFF
    if current_staff in staff_subject_map:
        keywords = staff_subject_map[current_staff]

        assignments = [
            a for a in assignments
            if a.subject and any(k in a.subject.lower() for k in keywords)
        ]

    data = []

    # ✅ LOOP THROUGH EXCEL STUDENTS ONLY
    for s in students_excel:

        name = s["NAME"]
        reg = str(s["REGISTER_NUMBER"]).strip().upper()

        student_data = {
            'name': name,
            'reg': reg,
            'year': "",
            'subject': "",
            'date': "",
            'a1': None,
            'a2': None,
            'a3': None,
            'a4': None,
        }

        # ✅ MATCH DB DATA WITH THIS STUDENT
        student_assignments = [
            a for a in assignments
            if str(a.register_number).strip().upper() == reg
        ]

        for a in student_assignments:

            db_reg = str(a.register_number).strip().upper()

            if db_reg == reg:

                student_data['year'] = a.year
                student_data['subject'] = a.subject
                student_data['date'] = a.date

                assignment_no = str(a.assignment_no).strip().lower()

                if "1" in assignment_no:
                    student_data['a1'] = a.assignment_file

                elif "2" in assignment_no:
                    student_data['a2'] = a.assignment_file

                elif "3" in assignment_no:
                    student_data['a3'] = a.assignment_file

                elif "4" in assignment_no:
                    student_data['a4'] = a.assignment_file

        data.append(student_data)

    return render(request, "staff_assignments.html", {
        'students': data,
        'section': section
    })

def staff_feedback(request):

    from .models import Feedback

    feedbacks = Feedback.objects.all().order_by("-id")

    return render(request, "staff_feedback.html", {
        "feedbacks": feedbacks
    })

def staff_office(request):

    group = "OFFICE"

    if request.method == "POST":

        message = request.POST.get("message")
        file = request.FILES.get("file")

        if message or file:
            GroupMessage.objects.create(
                group_name=group,
                sender="Staff",
                message=message if message else "",
                file=file
            )

        return redirect("staff_office")

    messages = GroupMessage.objects.filter(
        group_name=group
    ).order_by("time")

    return render(request, "staff_office.html", {"messages": messages})

def staff_timetable(request):
    return render(request,"staff_timetable.html")

def staff_no_due_select(request):
    return render(request, "staff_no_due_select.html")

from .models import NoDueVerification

def staff_no_due(request, class_name):

    from .models import NoDueVerification
    import pandas as pd
    import os
    from django.conf import settings

    # ✅ SAVE DATA ONLY IN POST
    if request.method == "POST":

        student_NAME = request.POST.get("student_NAME")
        REGISTER_NUMBER = request.POST.get("REGISTER_NUMBER")
        subject = request.session.get("user")   # ✅ FIXED
        status = request.POST.get("status")

        obj, created = NoDueVerification.objects.get_or_create(
            register_number=REGISTER_NUMBER,
            subject=subject,
            defaults={
                "student_name": student_NAME,
                "status": status
            }
        )

        if not created:
            obj.status = status
            obj.save()

    # ✅ BELOW THIS IS ONLY FOR DISPLAY (NO REGISTER_NUMBER HERE)

    if class_name == "A":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_a.xlsx")
    elif class_name == "B":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_b.xlsx")
    else:
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_c.xlsx")

    df = pd.read_excel(file_path)
    students = df.to_dict(orient="records")

    assignments = Assignment.objects.all()

    # CREATE MAP (BEST METHOD)
    assignment_map = {}

    for a in assignments:
        reg = str(a.register_number).strip().upper()

        if reg not in assignment_map:
            assignment_map[reg] = set()

        if a.assignment_no:
            assignment_map[reg].add(a.assignment_no)

    # ADD COUNT TO STUDENTS
    for s in students:
        reg = str(s["REGISTER_NUMBER"]).strip().upper()

        s["assignment_count"] = len(assignment_map.get(reg, []))

    current_staff = request.session.get("user")

    verifications = NoDueVerification.objects.filter(
        subject=current_staff
    )
    assignments = Assignment.objects.all()

    # CLEAN REGISTER NUMBER
    for a in assignments:
        a.register_number = str(a.register_number).strip().upper()


    return render(request, "staff_no_due.html", {
        "students": students,
        "verifications": verifications,
        "assignments": assignments,
        "class_name": class_name
    })
def staff_profile_verification(request):

    import pandas as pd
    import os
    from django.conf import settings
    from .models import StudentProfileVerification

    current_staff = request.session.get("user")

    # SAVE DATA
    if request.method == "POST":

        student_NAME = request.POST.get("student_NAME")
        REGISTER_NUMBER = request.POST.get("REGISTER_NUMBER")
        status = request.POST.get("status")

        obj, created = StudentProfileVerification.objects.get_or_create(
            register_number=REGISTER_NUMBER,
            staff_name=current_staff,
            defaults={
                "student_name": student_NAME,
                "status": status
            }
        )

        if not created:
            obj.status = status
            obj.save()

    # LOAD EXCEL
    file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_a.xlsx")
    df = pd.read_excel(file_path)
    students = df.to_dict(orient="records")

    # ONLY THIS STAFF DATA
    verifications = StudentProfileVerification.objects.filter(
        staff_name=current_staff
    )

    return render(request, "staff_profile_verification.html", {
        "students": students,
        "verifications": verifications
    })

def selection_page(request):
    return render(request, "selection.html")

def student_profile_verification(request, class_name):

    from .models import StudentProfileVerification
    import pandas as pd
    import os
    from django.conf import settings

    # SAVE DATA
    if request.method == "POST":

        student_NAME = request.POST.get("student_NAME")
        REGISTER_NUMBER = request.POST.get("REGISTER_NUMBER")
        staff_name = request.session.get("user")  # logged staff
        status = request.POST.get("status")

        obj, created = StudentProfileVerification.objects.get_or_create(
            register_number=REGISTER_NUMBER,
            staff_name=staff_name,
            defaults={
                "student_name": student_NAME,
                "status": status
            }
        )

        if not created:
            obj.status = status
            obj.save()

    # LOAD EXCEL
    if class_name == "A":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_a.xlsx")
    elif class_name == "B":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_b.xlsx")
    else:
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_c.xlsx")

    df = pd.read_excel(file_path)
    students = df.to_dict(orient="records")


    current_staff = request.session.get("user")

    verifications = StudentProfileVerification.objects.filter(
        staff_name=current_staff
    )

    return render(request, "student_profile_verification.html", {
        "students": students,
        "verifications": verifications,
        "class_name": class_name
    })
def student_profile_select(request):
    return render(request, "student_profile_select.html")

def staff_profile_select(request):
    return render(request, "staff_profile_select.html")

def staff_profile_verification(request, class_name):
    import pandas as pd
    import os
    from django.conf import settings
    from .models import StudentProfileVerification

    if request.method == "POST":
        student_name = request.POST.get("student_NAME")
        register_number = request.POST.get("REGISTER_NUMBER")
        staff_name = request.session.get("user")
        status = request.POST.get("status")

        obj, created = StudentProfileVerification.objects.get_or_create(
            register_number=register_number,
            staff_name=staff_name,
            defaults={
                "student_name": student_name,
                "status": status
            }
        )

        if not created:
            obj.status = status
            obj.save()

    # LOAD EXCEL
    if class_name == "A":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_a.xlsx")
    elif class_name == "B":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_b.xlsx")
    else:
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_c.xlsx")

    df = pd.read_excel(file_path)
    students = df.to_dict(orient="records")

    current_staff = request.session.get("user")

    verifications = StudentProfileVerification.objects.filter(
        staff_name=current_staff
    )

    return render(request, "student_profile_verification.html", {
        "students": students,
        "verifications": verifications,
        "class_name": class_name
    })
def select_class(request):
    return render(request, 'class_select.html')
def office_dashboard(request):
    return render(request, "office_dashboard.html")

def office_student_detail(request, reg):

    from .models import NoDueVerification

    verifications = NoDueVerification.objects.filter(register_number=reg)

    # office page → student should be FALSE
    is_student = False

    if request.method == "POST":
        office = request.POST.get("office")

        NoDueVerification.objects.filter(
            register_number=reg
        ).update(
            office_status=office
        )

    return render(request, "office_student_detail.html", {
        "verifications": verifications,
        "reg": reg,
        "is_student": is_student
    })

def office_students(request, class_name):

    import pandas as pd
    import os
    from django.conf import settings
    from .models import NoDueVerification

    # LOAD EXCEL
    if class_name == "A":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_a.xlsx")
    elif class_name == "B":
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_b.xlsx")
    else:
        file_path = os.path.join(settings.BASE_DIR, "myapps/data/final_cse_c.xlsx")

    df = pd.read_excel(file_path)
    students = df.to_dict(orient="records")

    final_students = []

    for s in students:
        reg = str(s["REGISTER_NUMBER"]).strip().upper()

        # get all verification rows for this student
        verifications = NoDueVerification.objects.filter(register_number=reg)

        verified_count = verifications.filter(status="Verified").count()

        # ✅ CHANGE THIS NUMBER BASED ON STAFF COUNT
        TOTAL_STAFF = 5

        is_fully_verified = verified_count == TOTAL_STAFF

        final_students.append({
            "name": s["NAME"],
            "reg": reg,
            "is_verified": is_fully_verified
        })

    return render(request, "office_students.html", {
        "students": final_students,
        "class_name": class_name
    })
def student_office(request):

    from .models import NoDueVerification

    reg = request.session.get("student_reg")

    verifications = NoDueVerification.objects.filter(
        register_number=reg
    )

    return render(request, "student_office_status.html", {
        "verifications": verifications,
        "reg": reg
    })
def student_office_status(request):

    from .models import NoDueVerification

    reg = request.session.get("student_reg")

    verifications = NoDueVerification.objects.filter(
        register_number=reg
    )

    is_student = True

    return render(request, "office_student_detail.html", {
        "verifications": verifications,
        "reg": reg,
        "is_student": is_student
    })

def syllabus_selection(request):
    return render(request,"syllabus_selection.html")


def view_syllabus(request,subject):

    subjects={
        "ai":("Artificial Intelligence","ai.pdf"),
        "ml":("Machine Learning","ml.pdf"),
        "cloud":("Cloud Computing","cloud.pdf"),
        "bigdata":("Big Data","bigdata.pdf"),
        "cyber":("Cyber Security","cyber.pdf"),
    }

    subject_name,file=subjects.get(subject)

    return render(request,"view_syllabus.html",{
        "subject":subject_name,
        "file":file
    })

