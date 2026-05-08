import sys
from PyQt6.QtWidgets import QApplication, QTabWidget, QVBoxLayout, QWidget, QMainWindow
from PyQt6.QtGui import QFont

# PyJHora UI කොටස් import කරගැනීම
try:
    from jhora.ui.panchangam import PanchangaWidget
    from jhora.ui.vedic_calendar import CalendarWidget
    from jhora.ui.horo_chart_tabs import ChartTabbed
    from jhora.ui.match_ui import MatchWidget
except ImportError:
    print("Error: PyJHora නිවැරදිව Install වී නොමැත. 'pip install PyJHora' ටයිප් කරන්න.")

class SinhalaAstrologyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # මෘදුකාංගයේ නම සහ වින්ඩෝ එකේ ප්‍රමාණය
        self.setWindowTitle("ජ්‍යොතිෂ්‍ය මෘදුකාංගය - 2026")
        self.setMinimumSize(1100, 850)

        # ප්‍රධාන Widget එක සහ Layout එක
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # ටැබ් පද්ධතිය (Tabs) නිර්මාණය
        self.tabs = QTabWidget()
        
        # සිංහල අකුරු ලස්සනට පෙන්වීමට Font එකක් සැකසීම
        font = QFont("Iskoola Pota", 11)
        self.tabs.setFont(font)

        # එක් එක් UI කොටස් (Widgets) වෙන වෙනම හදාගැනීම
        self.tab_charts = ChartTabbed()      # කේන්දර සටහන්
        self.tab_panchanga = PanchangaWidget()  # පංචාංගය
        self.tab_calendar = CalendarWidget()    # දින දසුන
        self.tab_match = MatchWidget()          # පොරොන්දම්

        # ටැබ් එකතු කිරීම (සිංහල නම් සහිතව)
        self.tabs.addTab(self.tab_charts, "කේන්දර සටහන (Charts)")
        self.tabs.addTab(self.tab_panchanga, "පංචාංගය (Panchangam)")
        self.tabs.addTab(self.tab_calendar, "දින දසුන (Calendar)")
        self.tabs.addTab(self.tab_match, "පොරොන්දම් ගැලපීම (Matching)")

        layout.addWidget(self.tabs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # පෙනුම තවත් වැඩි දියුණු කිරීමට Style එකක් සැකසීම
    app.setStyle("Fusion") 
    
    window = SinhalaAstrologyApp()
    window.show()
    sys.exit(app.exec())
