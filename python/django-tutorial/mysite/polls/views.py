from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from mysite.polls.models import Poll, Choice
##
##def index(request):
##    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
##    return render_to_response('polls/poll_list.html',
##                              {'latest_poll_list': latest_poll_list})
####    t = loader.get_template('polls/index.html')
####    c = Context({
####        'latest_poll_list': latest_poll_list,
####    })
####    return HttpResponse(t.render(c))
##
##def detail(request, poll_id):
##    p = get_object_or_404(Poll, pk=poll_id)
##    return render_to_response('polls/detail.html', {'poll': p},
##            context_instance = RequestContext(request))     # CSRF
##
##def results(request, poll_id):
##    p = get_object_or_404(Poll, pk=poll_id)
##    return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Poll ??????????????
        return render_to_response('polls/poll_detail.html', {
            'object': p,
            'error_message': "????????????",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # ???? Back ??????????????????????
        # ???POST ????????????????
        # HttpResponseRedirect ??????????
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
    
    
