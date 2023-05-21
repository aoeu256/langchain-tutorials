
try:
    import library_name
except ImportError as e:
    library_name = e.name
    import pip
    pip.main(['install', library_name])
    import library_name
