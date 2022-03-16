from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
main_menu = KeyboardButton('Main menu')

# Кнопки главного меню
btn_full = KeyboardButton('Full')
btn_manipulator = KeyboardButton('Manipulator')
btn_unpacker = KeyboardButton('Unpacker')
#btn_YRFfiles = KeyboardButton('\U0001F4C1YRFfiles')

# Кнопки раздела Follow-up
btn_electronics = KeyboardButton('Electronics')
btn_design = KeyboardButton('Design')
btn_software = KeyboardButton('Software')
btn_decor = KeyboardButton('Decor')
btn_sprint = KeyboardButton('\U0001F3C3Sprint')
btn_other = KeyboardButton('Other')

# Кнопки раздела Manipulator
btn_storage = KeyboardButton('Storage')
btn_calibration = KeyboardButton('Calibration')

# Кнопки раздела Providers
btn_hardware = KeyboardButton('Hardware')
btn_parts = KeyboardButton('Parts')
btn_electrica = KeyboardButton('Electrica')
btn_produced = KeyboardButton('Produced')

# Кнопки раздела YRFfiles
btn_documents = KeyboardButton('Documents')
btn_googledocs = KeyboardButton('GoogleDocs')
btn_chats = KeyboardButton('Chats')


# Кнопки раздела YRFfiles->Documents
btn_doverennost = KeyboardButton('Doverennost')
btn_reqvisits = KeyboardButton('Reqvisits')

# Кнопки раздела YRFfiles->GoogleDocs
btn_bom = KeyboardButton('BOM')
btn_genplan = KeyboardButton('Генплан YFR')
btn_drive = KeyboardButton('GoogleDrive')

# Кнопки подраздела Providers->Parts
btn_profiles = KeyboardButton('Profiles')
btn_screws = KeyboardButton('Screws')
btn_corner = KeyboardButton('Corners')
btn_sheets = KeyboardButton('Sheets')


# Кнопки подраздела Providers->Hardware
btn_motors = KeyboardButton('Motors')
btn_reductors = KeyboardButton('Reductors')
btn_drivers = KeyboardButton('Drivers')
btn_servo = KeyboardButton('Servo')


# Кнопки подраздела Providers->Electrica
btn_wires = KeyboardButton('Wires')
btn_connectors = KeyboardButton('Connectors')
btn_rele = KeyboardButton('Rele')


# Кнопки подраздела Providers->Produce
btn_lazermetal = KeyboardButton('Laser metal')
btn_lazeracril = KeyboardButton('Laser acril')


# Кнопки раздела myTasks
btn_todo = InlineKeyboardButton(text='Поставленные(0)', callback_data='dsc')
btn_doing = InlineKeyboardButton(text='Выполняемые(0)', callback_data='zc')
btn_notaprove = InlineKeyboardButton(text='Ожидают подтверждения(0)', callback_data='ad')
btn_uaprove = InlineKeyboardButton(text='Нужно подтвердить(0)', callback_data='zxcv')
btn_aprove = InlineKeyboardButton(text='Ожидают принятия(0)', callback_data='zcxcz')


# Кнопки раздела robot control
btn_A1 = KeyboardButton('A_1')
btn_B1 = KeyboardButton('B_1')
btn_C1 = KeyboardButton('C_1')
btn_D1 = KeyboardButton('D_1')
btn_E1 = KeyboardButton('E_1')
btn_F1 = KeyboardButton('F_1')
btn_A2 = KeyboardButton('A_2')
btn_B2 = KeyboardButton('B_2')
btn_C2 = KeyboardButton('C_2')
btn_D2 = KeyboardButton('D_2')
btn_E2 = KeyboardButton('E_2')
btn_F2 = KeyboardButton('F_2')
btn_A3 = KeyboardButton('A_3')
btn_B3 = KeyboardButton('B_3')
btn_C3 = KeyboardButton('C_3')
btn_D3 = KeyboardButton('D_3')
btn_E3 = KeyboardButton('E_3')
btn_F3 = KeyboardButton('F_3')
btn_A4 = KeyboardButton('A_4')
btn_B4 = KeyboardButton('B_4')
btn_C4 = KeyboardButton('C_4')
btn_D4 = KeyboardButton('D_4')
btn_E4 = KeyboardButton('E_4')
btn_F4 = KeyboardButton('F_4')
btn_A5 = KeyboardButton('A_5')
btn_B5 = KeyboardButton('B_5')
btn_C5 = KeyboardButton('C_5')
btn_D5 = KeyboardButton('D_5')
btn_E5 = KeyboardButton('E_5')
btn_F5 = KeyboardButton('F_5')
btn_A6 = KeyboardButton('A_6')
btn_B6 = KeyboardButton('B_6')
btn_C6 = KeyboardButton('C_6')
btn_D6 = KeyboardButton('D_6')
btn_E6 = KeyboardButton('E_6')
btn_F6 = KeyboardButton('F_6')
btn_A7 = KeyboardButton('A_7')
btn_B7 = KeyboardButton('B_7')
btn_C7 = KeyboardButton('C_7')
btn_D7 = KeyboardButton('D_7')
btn_E7 = KeyboardButton('E_7')
btn_F7 = KeyboardButton('F_7')
btn_A8 = KeyboardButton('A_8')
btn_B8 = KeyboardButton('B_8')
btn_C8 = KeyboardButton('C_8')
btn_D8 = KeyboardButton('D_8')
btn_E8 = KeyboardButton('E_8')
btn_F8 = KeyboardButton('F_8')
btn_A9 = KeyboardButton('A_9')
btn_B9 = KeyboardButton('B_9')
btn_C9 = KeyboardButton('C_9')
btn_D9 = KeyboardButton('D_9')
btn_E9 = KeyboardButton('E_9')
btn_F9 = KeyboardButton('F_9')
btn_A10 = KeyboardButton('A_10')
btn_B10 = KeyboardButton('B_10')
btn_C10 = KeyboardButton('C_10')
btn_D10 = KeyboardButton('D_10')
btn_E10 = KeyboardButton('E_10')
btn_F10 = KeyboardButton('F_10')
btn_A11 = KeyboardButton('A_11')
btn_B11 = KeyboardButton('B_11')
btn_C11 = KeyboardButton('C_11')
btn_D11 = KeyboardButton('D_11')
btn_E11 = KeyboardButton('E_11')
btn_F11 = KeyboardButton('F_11')
btn_A12 = KeyboardButton('A_12')
btn_B12 = KeyboardButton('B_12')
btn_C12 = KeyboardButton('C_12')
btn_D12 = KeyboardButton('D_12')
btn_E12 = KeyboardButton('E_12')
btn_F12 = KeyboardButton('F_12')
btn_A13 = KeyboardButton('A_13')
btn_B13 = KeyboardButton('B_13')
btn_C13 = KeyboardButton('C_13')
btn_D13 = KeyboardButton('D_13')
btn_E13 = KeyboardButton('E_13')
btn_F13 = KeyboardButton('F_13')
btn_A14 = KeyboardButton('A_14')
btn_B14 = KeyboardButton('B_14')
btn_C14 = KeyboardButton('C_14')
btn_D14 = KeyboardButton('D_14')
btn_E14 = KeyboardButton('E_14')
btn_F14 = KeyboardButton('F_14')


kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_full = ReplyKeyboardMarkup(resize_keyboard=True)
kb_manipulator = ReplyKeyboardMarkup(resize_keyboard=True)
kb_colomn = ReplyKeyboardMarkup(resize_keyboard=True)


kb_manipulator.add(btn_storage).add(btn_calibration).add(main_menu)
kb_menu.add(btn_full).add(btn_manipulator).add(btn_unpacker)
kb_manipulator.add(main_menu)

kb_colomn.row(btn_A1, btn_B1, btn_C1, btn_D1, btn_E1, btn_F1)
kb_colomn.row(btn_A2, btn_B2, btn_C2, btn_D2, btn_E2, btn_F2)
kb_colomn.row(btn_A3, btn_B3, btn_C3, btn_D3, btn_E3, btn_F3)
kb_colomn.row(btn_A4, btn_B4, btn_C4, btn_D4, btn_E4, btn_F4)
kb_colomn.row(btn_A5, btn_B5, btn_C5, btn_D5, btn_E5, btn_F5)
kb_colomn.row(btn_A6, btn_B6, btn_C6, btn_D6, btn_E6, btn_F6)
kb_colomn.row(btn_A7, btn_B7, btn_C7, btn_D7, btn_E7, btn_F7)
kb_colomn.row(btn_A8, btn_B8, btn_C8, btn_D8, btn_E8, btn_F8)
kb_colomn.row(btn_A9, btn_B9, btn_C9, btn_D9, btn_E9, btn_F9)
kb_colomn.row(btn_A10, btn_B10, btn_C10, btn_D10, btn_E10, btn_F10)
kb_colomn.row(btn_A11, btn_B11, btn_C11, btn_D11, btn_E11, btn_F11)
kb_colomn.row(btn_A12, btn_B12, btn_C12, btn_D12, btn_E12, btn_F12)
kb_colomn.row(btn_A13, btn_B13, btn_C13, btn_D13, btn_E13, btn_F13)
kb_colomn.row(btn_A14, btn_B14, btn_C14, btn_D14, btn_E14, btn_F14)

