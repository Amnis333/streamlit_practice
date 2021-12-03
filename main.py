import streamlit as st
import numpy as np  
import pandas as pd 
from PIL import Image
from streamlit.proto.Button_pb2 import Button
import time 

st.title('Streamlit超入門')

#st.write('Interactive WIdgets')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar =st.progress(0)
'Done!!'

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


#if st.checkbox('ShowImage'):
    
#    img = Image.open('奥入瀬.jpg')
#    st.image(img,caption='奥入瀬渓流',use_column_width=True)

#option = st.selectbox(
#    'あなたが好きな数字を教えてください。',
#    list(range(1,11))
#)

#'あなたの好きな数字は',option,'です'







left_column,right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
    

expander = st.expander('問い合わせ')

expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください。')

# 'あなたの趣味は',text,'です'


# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディションは',condition,'です'


df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
    )

st.map(df)

#st.table(df.style.highlight_max(axis=0))


"""

# 章
## 節
### 項

```python

import streamlit as st
import numpy as np  
import pandas as pd 

```

"""

