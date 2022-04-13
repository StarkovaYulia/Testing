from mirrorClock import mirrorClock
import sqlite3 as sl

class DatabaseTime:
    def __init__(self):
        self.con = sl.connect('my_test.db')
        self.cur = self.con.cursor()

    def createDB(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS CountTime( timeMirror text,  timeReal text)')
        self.cur.execute('DELETE FROM CountTime')

    def convertTimeAndAddToDB(self, mirrorTime):
        self.createDB()
        clock = mirrorClock()

        timeReal = clock.what_is_the_time(mirrorTime)
        self.cur.execute("INSERT INTO CountTime(timeMirror, timeReal) VALUES (?, ?)", (mirrorTime, timeReal))

        self.con.close()

        return timeReal




