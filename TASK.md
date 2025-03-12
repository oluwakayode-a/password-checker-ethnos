Live Coding Task for Engineer Interview (Django, Celery, PostgreSQL, Caching, Sentry)


Task Title: Secure Password Leak Detection System Estimated Time: ⏳ 1hr 30min Goal: Implement a simple API where users can check if their password has been leaked using the HIBP (Have I Been Pwned) API. The system should efficiently handle requests with Celery (background task processing), PostgreSQL, caching, and Sentry for error logging.


 Task Breakdown:

	•	Set up a Django API Endpoint (/check-password/)
	•	The endpoint should accept a password as input.
	•	The API should compute the SHA1 hash prefix of the password and query the HIBP API.
	•	If the password is found in the breach list, return { "status": "leaked", "count": X }.
	•	If not, return { "status": "safe" }.

	•	Process Password Leak Checks Asynchronously with Celery

	•	Ensure the password check runs as a Celery task, so the API immediately responds with a task ID.
	•	Implement a status check endpoint (/task-status/<task_id>/) where users can poll task progress.
	•	Use PostgreSQL for Storing Password Check Results

	•	Create a model PasswordCheckResult to store password hash prefix and breach count.
	•	Before making an API request, check if the password has been checked before (avoid redundant calls).
	•	Implement Caching with Redis (or any preferred caching system)

	•	Cache password hash prefix results for 24 hours to reduce API calls.
	•	Use Django’s built-in cache framework.
	•	Integrate Sentry for Error Logging

	•	Configure Sentry to capture exceptions (e.g., API failures, Celery task crashes).
	•	Ensure Celery errors are also logged in Sentry.



-- Check password against the list of constatnts.