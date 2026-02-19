import band_schedule
import memory_graph as mg
import io
import contextlib
import softeng

def remove_whitespaces(s):
    return ''.join(s.split())

def test_band_schedule():
    f = io.StringIO()
    output = ""
    try:
        with contextlib.redirect_stdout(f):
            band_schedule.main()
        output = f.getvalue()
    except Exception as e:
        print(f"An error occurred: {e}")
    assert softeng.fixedhash(remove_whitespaces(output)) == "e2dd4d1f1c237d056a83b6c1b828d937212d69111e1b932cc0b96ead93b425e9"
