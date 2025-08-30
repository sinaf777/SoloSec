from django.shortcuts import render, get_object_or_404, redirect
from .models import Challenge,  DIFFICULTY_POINTS 
from django.contrib.auth.decorators import login_required
from users.models import Badge

# Create your views here.
@login_required
def challenge_list(request):
    challenges = Challenge.objects.all()
    return render (request, "challenges/list.html", {"challenges": challenges})

@login_required
def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    user = request.user
    message = None

    if request.method == "POST":
        submitted_flag = request.POST.get("flag")
        if submitted_flag == challenge.flag:
            if challenge not in user.solved.all():
                # Add challenge to solved list
                user.solved.add(challenge)
                # Add points based on difficulty
                user.score += DIFFICULTY_POINTS.get(challenge.difficulty, 0)
                user.save()
                message = f"✅ Correct! You earned {DIFFICULTY_POINTS[challenge.difficulty]} pts."

                # Check for newly unlocked badges
                badges = Badge.objects.filter(min_score__lte=user.score)
            else:
                message = "⚠️ You already solved this challenge."
        else:
            message = "❌ Incorrect flag. Try again."

    # Always send solved challenges and badges for dynamic update
    solved_challenges = user.solved.all()
    badges = Badge.objects.filter(min_score__lte=user.score)

    return render(request, "challenges/challenge_detail.html", {
        "challenge": challenge,
        "message": message,
        "solved_challenges": solved_challenges,
        "badges": badges,
        "user": user,
    })