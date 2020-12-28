def make_price(st):    
    st = 'Экран:8\xa0″, 1280x800\xa0пикс, 189\xa0ppiПамять:16\xa0ГБ, слот microSDКамера:5\xa0МП, камера для видеозвонковHardware:4\xa0ядер(а), 1.4\xa0ГГц, оперативка 2\xa0ГБАккумулятор:4800\xa0мАчКорпус:металл, 350\xa0г, толщина 8\xa0мм'
    st = st.replace(u'\xa0', ' ')
    st = st.replace('SDК', 'SD, К')
    st = st.replace('ppiП', 'ppi, П')
    st = st.replace('Hardware', ' встроенная')
    st = st.replace('я:4', 'я, 4')
    st = st.replace('ГБАк', 'ГБ, Ак')
    st = st.replace('АчК', 'Ач, К')
    st = st.replace('″, ', '″; ')
    inform = [i for i in st.split(',')]

    return(inform)