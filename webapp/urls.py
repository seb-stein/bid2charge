from django.conf.urls import patterns, url
from webapp import views

urlpatterns = patterns('',
	url(r'^do.login/$', views.do_login),
	url(r'^home/$', views.home, name = 'home'),
	url(r'^instructions/$', views.instructions, name = 'instructions'),
	url(r'^run_simple_auction/$', views.run_simple_auction),
	url(r'^run_uniform_auction/$', views.run_uniform_auction),
	url(r'^run_progressive_auction/$', views.run_progressive_auction),
	url(r'^auction_result/$', views.auction_result),
	url(r'^delivery/$', views.delivery, name='delivery'),
	url(r'^getTasksToPerform/$', views.getTasksToPerform),
	url(r'^getOptimalTaskSets/$', views.getOptimalTaskSets),
	url(r'^updateUserToNextDay/$', views.updateUserToNextDay),
	url(r'^skip_auction/$', views.skipAuction),
	url(r'^game_complete/$', views.gameComplete),
	url(r'^checkIfAuctionTookPlaceToday/$', views.auctionTookPlaceToday),
	url(r'^logTaskClickEvent/$', views.logTaskClickEvent),
	url(r'^leaderboard/$', views.leaderboard),
	url(r'^history/$', views.history),
	url(r'^becomeEvGuru/$', views.becomeEvGuru),
	url(r'^settings/$', views.settings),
	url(r'^resetBalancePage/$', views.resetBalancePage),
	url(r'^updateSettings/$', views.updateSettings),
	url(r'^rules/$', views.quiz),
	url(r'^survey/$', views.survey),
	url(r'^hit_done/$', views.hitDone),
	url(r'^skipQuiz/$', views.aamasSkipQuiz),
	url(r'^changeMechanism/$', views.aamasChangeMechanism),
	url(r'^changeExperiment/$', views.aamasChangeExperiment),
	url(r'^resetGame/$', views.aamasResetGame),
	url(r'^orchidNewPlayer/$', views.orchidNewPlayer),
	url(r'^orchidExistingPlayer/$', views.orchidExistingPlayer),
	url(r'^orchidNewGame/$', views.orchidNewGame),
	url(r'^orchidLeaderboard/$', views.orchidLeaderboard),
	url(r'^orchidPerformance/$', views.orchidPerformance)
)
