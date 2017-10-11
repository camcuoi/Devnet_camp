session_attended = {"sessions":[1011,2344,1234,3456,7891,32411,56781,9032,1234]}
count = 0
my_session = [1011,2344]
for session in session_attended["sessions"]:
	if my_session[0] == session:
		count = count +1
	if my_session[1] == session:
		count = count +1

print("I attended", count, "sessions")
