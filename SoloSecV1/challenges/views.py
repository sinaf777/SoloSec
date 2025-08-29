from django.shortcuts import render, get_object_or_404, redirect
from .models import Challenge
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def challenge_list(request):
    challenges = Challenge.objects.all()
    return render (request, "challenges/list.html", {"challenges": challenges})

def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    message = ""
    
    if request.method == "POST":
        submitted_flag = request.POST.get("flag")
        if submitted_flag == challenge.flag:
            if challenge not in request.user.solved.all():
                request.user.solved.add(challenge)
                request.user.score += challenge.points
                request.user.save()
                message = "✅ Correct flag! Challenge solved."
            else:
                message = "⚠️ You've already solved this challenge."
        else:
            message = "❌ Incorrect flag. Try again."

    return render(request, "challenges/detail.html", {"challenge": challenge, "message": message})