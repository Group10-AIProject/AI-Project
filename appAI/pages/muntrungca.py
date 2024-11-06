import streamlit as st
import base64
from pathlib import Path
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import base64


st.set_page_config(
    page_title="KHÁM PHÁ MỤN TRỨNG CÁ",
    page_icon="🧊",
    layout="wide",
)

# Hàm chuyển hình ảnh sang bytes và mã hóa base64
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# Hàm tạo HTML cho hình ảnh đã mã hóa base64
def img_to_html(img_path, width="100px", height="80px"):
    img_html = f"<img src='data:image/png;base64,{img_to_bytes(img_path)}' style='width:{width}; height:{height};'>"
    return img_html

# Sử dụng hàm img_to_html để mã hóa logo và hình ảnh bên phải
anhbia = img_to_html('biamuntrungca.jpeg', width="1600px", height="350px")
logo_html = img_to_html('logo.png', width="100px", height="80px")  # Thay đường dẫn này bằng logo của bạn


css_code = """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        background-color: #ffffff;
        padding: 1px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);

    }
    .navbar a {
        text-decoration: none;
        color:  #FF8343;
        padding: 16px;
        margin-top: 35px;
        font-size: 16px;
        font-weight: bold;
    }
    .navbar a:hover {
        color: #007bff;
        text-decoration: underline;
    }
    </style>
"""
st.markdown(css_code, unsafe_allow_html=True)
st.markdown(f"""
    <div class="navbar">
        <div class="logo">
            {logo_html}
        </div>
        <div style= "margin-top: 33px";>
            <a href="#home">Home</a>
            <a href="#about">Trải nghiệm Derm Insight</a>
            <a href="#projects">Vấn đề da liễu</a>
            <a href="#services">About us</a>
        </div>
    </div>

""", unsafe_allow_html=True)

st.markdown(f"""
            {anhbia}
     
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .breadcrumb-nav {
            display: flex;
            margin-bottom: 1px;
            margin-top: 15px;
        }
        
        .breadcrumb-nav ol {
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }
        
        .breadcrumb-nav li {
            display: inline-flex;
            align-items: center;
            font-size: 0.875rem;
            color: #4A5568;
            font-weight: 600;
        }

        .breadcrumb-nav li a {
            color: #4A5568;
            text-decoration: none;
        }

        .breadcrumb-nav li a:hover {
            color: #FF8343;
        }

        .breadcrumb-nav .icon {
            width: 12px;
            height: 12px;
            margin-right: 4px;
            fill: currentColor;
        }

        .breadcrumb-divider {
            color: #A0AEC0;
            margin-left: 4px;
        }

        .page-title {
            margin-top: 25px;
            margin-bottom: 5px;
            font-size: 1.875rem;
            font-weight: 800;
            color: #1A202C;
        }

        .breadcrumb-nav li .current {
            color: #718096;
            
        }
    </style>
    """, unsafe_allow_html=True)

    # HTML structure
st.markdown("""
        <nav class="breadcrumb-nav" aria-label="Breadcrumb">
        <ol>
            <li>
            <a href="http://localhost:8501" class="home-link">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                <path d="m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z"/>
                </svg>
                Home
            </a>
            </li>
            <span class="breadcrumb-divider">/</span>
            <li>
            <a href="#" class="current">Vấn đề da liễu</a>
            </li>
            <span class="breadcrumb-divider">/</span>
            <li>
            <a href="" class="current">Mụn trứng cá</a>
            </li>
        </ol>
        </nav>

    """, unsafe_allow_html=True)

# Header with orange gradient text
header_html = """
<h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
    TẤT CẢ VỀ <span style="background: linear-gradient(to right, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 35px;">MỤN TRỨNG CÁ NẶNG (AV) </span>
</h1>
<p class="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">
   Mụn trứng cá nặng, hay còn gọi là Acne Vulgaris, là một tình trạng da phổ biến, thường xuất hiện trong tuổi dậy thì nhưng cũng có thể xảy ra ở người lớn. Đây là một dạng mụn trứng cá nghiêm trọng, thường gây ra các nốt mụn lớn, sưng đỏ và đau đớn. Mụn trứng cá nặng có thể để lại sẹo và các dấu hiệu trên da, ảnh hưởng đến tâm lý và chất lượng cuộc sống của người mắc phải.
"""

# Displaying the header in Streamlit
st.markdown(header_html, unsafe_allow_html=True)

# Tiêu đề phụ
st.markdown("""
    <p style="font-size: 24px; color: #FF8343; font-weight: bold; margin-top: 20px;">
        Lời khuyên cho bệnh mụn trứng cá nặng:
    </p>
""", unsafe_allow_html=True)

# Nội dung mô tả với các gạch đầu dòng
st.markdown("""
    <ul style="font-size: 18px; line-height: 1.6;">
        <li>Thăm khám bác sĩ da liễu để nhận chẩn đoán và điều trị phù hợp.</li>
        <li>Chăm sóc da nhẹ nhàng, rửa mặt với sản phẩm dịu nhẹ, không nặn mụn.</li>
        <li>Dùng sản phẩm không gây bít tắc lỗ chân lông.</li>
        <li>Ăn uống lành mạnh, hạn chế đồ ngọt và sữa.</li>
        <li>Giảm căng thẳng và uống đủ nước.</li>
        <li>Bảo vệ da khỏi ánh nắng với kem chống nắng SPF 30+.</li>
    </ul>
""", unsafe_allow_html=True)

st.write("")
st.write("")

col1, col2 = st.columns([1, 2])

# Left column with main headings
with col1:
    st.subheader("Các chủ đề")
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">1</div>
        <div style="font-size: 16px; ">Mụn trứng cá nặng là gì?</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">2</div>
        <div style="font-size: 16px; ">Nguyên nhân nào gây ra mụn trứng cá?</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">3</div>
        <div style="font-size: 16px; ">Cách điều trị mụn trứng cá nặng</div>
    </div>
    """, unsafe_allow_html=True)
# Right column with detailed content for each heading
with col2:
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Mụn trứng cá nặng là gì?</p>
        <p style="font-size: 16px;">Mụn trứng cá nặng là tình trạng da xuất hiện nhiều mụn nhọt do sự tắc nghẽn nang lông kết hợp nhiễm khuẩn P.acnes và phản ứng viêm quá mức, trong trường hợp này mụn thường có mủ, sưng viêm to và gây đau nhức, khó chịu, thậm chí là có gốc sâu và áp xe hợp thành đường dò.
</p>
        <p style="font-size: 16px;">Loại mụn này thường xuyên xuất hiện ở mặt, tuy nhiên cũng có thể lan rộng ra các vùng khác trên cơ thể như ngực, vai, lưng. Mặc dù bệnh có thể xảy ra ở mọi đối tượng, nhưng tình trạng này thường gặp nhất ở lứa tuổi thanh thiếu niên.
</p>
    </div>
    """, unsafe_allow_html=True)

    # Mụn do nội tiết tố hoạt động như thế nào?
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Nguyên nhân nào gây ra mụn trứng cá?</p>
        <p style="font-size: 16px;">Yếu tố nguyên nhân gây nên mụn trứng cá nặng thông thường ở các trường hợp mụn trứng cá chuyển biến nặng hơn có thể do cơ địa hoặc điều trị mụn không đúng cách. Mụn trứng cá dạng nặng hay gặp ở nam nhiều hơn nữ và có yếu tố di truyền nếu trong gia đình cũng có người bị mụn trứng cá nặng.
        <p style="font-size: 16px;">Tuyệt đối không tự điều trị tại nhà và sử dụng thuốc của người thân để chữa mụn trứng cá nặng vì có thể làm tình trạng trở nên tồi tệ hơn. Hãy đến gặp bác sĩ để được chẩn đoán và điều trị thích hợp.
</p>
        <p style="font-size: 16px;">Ngoài ra, một số thói quen xấu như giữ gìn vệ sinh da không sạch sẽ, thường xuyên đưa tay lên mặt hoặc tự ý nặn mụn cũng làm cho tình trạng da trở nên nặng hơn.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Cách điều trị mụn trứng cá nặng</p>
        <p style="font-size: 16px;"> Có nhiều cách điều trị mụn trứng cá dạng nặng, bác sĩ sẽ chỉ định sử dụng các loại thuốc tùy vào tình trạng của bệnh nhân.</p>
        <p style="font-size: 16px;"> - Benzoyl peroxide hoặc dung dịch bôi có vitamin A giúp hạn chế tắc nghẽn lỗ chân lông và ngăn sự xâm nhập của vi khuẩn. </p>
        <p style="font-size: 16px;"> - Thuốc kháng sinh thoa tại chỗ nhằm hạn chế sự phát triển của vi khuẩn P.acnes ở bệnh nhân có mụn trứng cá dạng nặng.</p>
        <p style="font-size: 16px;"> - Retinoids bôi tại chỗ giúp làm thông thoáng lỗ chân lông, ngăn sự hình thành của mụn đầu đen và mụn đầu trắng.</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("< BACK"):
        st.switch_page("pages/Home.py")
