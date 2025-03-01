./exampleMidi.py
du --bytes test.mid
xxd test.mid | head
pmidi -p "16:0" test.mid
