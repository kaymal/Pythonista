import datetime as dt
import ui

date_picker = ui.DatePicker()
date_picker.mode = ui.DATE_PICKER_MODE_DATE
date_picker.date = dt.datetime.strptime('01/01/2019', '%d/%m/%Y')
date_picker.background_color = 'white'

date_picker.present()
