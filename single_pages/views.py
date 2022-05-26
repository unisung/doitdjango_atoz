from django.shortcuts import render
from blog.models import Post


def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3] #0,1,2

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )


def about_me(request):
    lead_content ='음악과 컴퓨터와 수영을 좋아합니다. 데이터분석으로 돈을 벌고, 퇴근 후에는 운동을 하거나 책을 쓰면서 지냅니다.'
    work_history=['크고좋은회사 - 빅데이터분석(2019.10~)','모모공공기관(2016.02 ~ 2019.09)']
    education_history=[
                       '공학박사, 장고공학(Django Engineering), 파이썬대학교(2010.03 ~2015.09)',
                       '공학석사, 장고공학(Django Engineering), 파이썬대학교(2007.09 ~2009.08)',
                       '공학학사, 장고공학(Django Engineering), 파이썬대학교(2003.03~2007.08)',
                     ]
    publish_history=['DO IT DJANGO, 이지스퍼블리싱(2020) ']

    card_titles = [{"title":"파이썬으로 통계업무 자동화하기 [PYCON 2017]",
                        "content":"Python, Django, Pandas, python-docx로 통계업무 자동화한 내용을 파이콘에서 발표했습니다",
                        "img":"pycon_sy_2017.png",
                        "target":"#pycon2017",
                        "id":"pycon2017"},
                       {"title": "파이썬 사용자를 위한 웹개발 입문 A to Z Django + Bootstrap",
                      "content": "파이썬 웹개발에 대한 인프런 동영상 강의입니다.",
                        "img":"inflearn_django2.png",
                        "target":"#inflearnDjango",
                        "id":"inflearnDjango"},
                       {"title": "직장인을 위한 프로그래밍 입문과 업무자동화 활용",
                    "content": "파이썬 업무자동화에 대한 인프런 동영상 강의입니다..",
                    "img": "automation_python.png",
                    "target":"#automationPython",
                    "id":"automationPython"},

                   ]


    return render(
        request,
        'single_pages/about_me.html',
        {'lead':lead_content, "work_history":work_history,
           "education_history":education_history, "publish_history":publish_history,
         "card_titles":card_titles}

    )