from scheduler import scheduler

def test_scheduler():
    jobs = scheduler.get_jobs()
    assert len(jobs) == 1
    assert jobs[0].name == "process_files"
