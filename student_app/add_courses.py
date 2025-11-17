import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_app.settings')
django.setup()

from courses.models import Course

# Clear existing courses
Course.objects.all().delete()

# Add new courses
courses_data = [
    {
        'name': 'BBIT - Bachelor of Business Information Technology',
        'description': 'A comprehensive degree program covering software development, database management, systems analysis, and IT business strategy. Students learn practical programming skills while understanding how technology drives business innovation.',
        'instructor': 'Prof. James Kariuki',
        'credits': 120
    },
    {
        'name': 'CNS - Computer Network Security',
        'description': 'Advanced course focusing on network architecture, cybersecurity protocols, ethical hacking, and security infrastructure. Covers firewall management, intrusion detection systems, and security auditing.',
        'instructor': 'Dr. Sarah Ndung\'u',
        'credits': 45
    },
    {
        'name': 'Software Engineering',
        'description': 'Learn the principles and practices of software development lifecycle. Covers design patterns, testing methodologies, version control, agile development, and project management for software teams.',
        'instructor': 'Dr. Michael Ochieng',
        'credits': 60
    },
    {
        'name': 'Finance',
        'description': 'Introduction to financial management, accounting principles, investment analysis, and corporate finance. Covers financial statements, budgeting, and financial decision-making in organizations.',
        'instructor': 'Prof. Grace Mwangi',
        'credits': 48
    }
]

for course_data in courses_data:
    Course.objects.create(**course_data)
    print(f"✓ Created: {course_data['name']}")

print(f"\nTotal courses: {Course.objects.count()}")
