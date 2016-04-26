# Set up the app
config:
	pip install -r requirements.txt  # Install Python dependencies
	cd frontend && bower install  # Install front-end dependencies


# Run the app (intended for develpoment)
run:
	redis-server&  # Start the local Redis server to the background
	python shatup.py run  # Run ShatUp
