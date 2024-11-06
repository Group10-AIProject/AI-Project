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
    page_title="KHÁM PHÁ BỆNH DÀY SỪNG",
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
anhbia = img_to_html('biadaysung.jpg', width="1600px", height="350px")
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
            <a href="http://localhost:8501/Home" class="home-link">
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
            <a href="#" class="current">Bệnh dày sừng quang hoá</a>
            </li>
        </ol>
        </nav>

    """, unsafe_allow_html=True)

# Header with orange gradient text
header_html = """
<h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
    TẤT CẢ VỀ <span style="background: linear-gradient(to right, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 35px;">BỆNH DÀY SỪNG QUANG HOÁ (AK) </span>
</h1>
<p class="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">
    Actinic Keratosis là một bệnh ngoài da phổ biến ảnh hưởng đến nhiều người. Nó phát sinh do da tiếp xúc kéo dài với ánh sáng mặt trời hoặc tia cực tím. Các mảng hoặc tổn thương thô ráp có vảy trên da là đặc điểm của tổn thương của bệnh. Các yếu tố dễ bị tổn thương thường được coi là triệu chứng tiền ung thư. Nếu không được phát hiện sớm và điều trị kịp thời có thể dẫn đến ung thư da tế bào vảy.
</p>
"""

# Displaying the header in Streamlit
st.markdown(header_html, unsafe_allow_html=True)

# Tiêu đề phụ
st.markdown("""
    <p style="font-size: 24px; color: #FF8343; font-weight: bold; margin-top: 20px;">
        Lời khuyên cho bệnh dày sừng quang hoá:
    </p>
""", unsafe_allow_html=True)

# Nội dung mô tả với các gạch đầu dòng
st.markdown("""
    <ul style="font-size: 18px; line-height: 1.6;">
        <li>Hạn chế tiếp xúc với ánh nắng mặt trời: Tránh ra ngoài vào giờ nắng gắt (thường từ 10 giờ sáng đến 4 giờ chiều).</li>
        <li>Sử dụng kem chống nắng: Chọn kem chống nắng phổ rộng với SPF từ 30 trở lên và thoa đều trên da ít nhất 15-30 phút trước khi ra ngoài. Bôi lại sau mỗi 2 giờ hoặc sau khi bơi lội hay đổ mồ hôi.</li>
        <li>Mặc đồ bảo vệ: Đội mũ rộng vành, đeo kính râm và mặc quần áo dài tay để bảo vệ da.</li>
        <li>Kiểm tra da định kỳ: Tự kiểm tra da thường xuyên và đến gặp bác sĩ da liễu để thăm khám, đặc biệt nếu phát hiện mảng da thay đổi về kích thước, màu sắc, hoặc gây khó chịu.</li>
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
        <div style="font-size: 16px; ">Bệnh dày sừng ánh sáng là gì?</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">2</div>
        <div style="font-size: 16px;">Những dấu hiệu và triệu chứng của bệnh dày sừng ánh sáng là gì?</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">3</div>
        <div style="font-size: 16px;">Nguyên nhân nào gây ra bệnh dày sừng ánh sáng?</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">4</div>
        <div style="font-size: 16px;">Những yếu tố nào làm tăng nguy cơ mắc bệnh dày sừng ánh sáng?</div>
    </div>
    """, unsafe_allow_html=True)
# Right column with detailed content for each heading
with col2:
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Bệnh dày sừng ánh sáng là gì?</p>
        <p style="font-size: 16px;">Bệnh dày sừng ánh sáng (actinic keratosis) là gì? Đây là tình trạng da bị thô ráp, có vảy khi tiếp xúc với mặt trời, đặc biệt là trên mặt, tay, cánh tay và cổ. Căn bệnh này thường gặp ở những người da trắng, mắt xanh.
</p>
        <p style="font-size: 16px;">Trong hầu hết các trường hợp, bệnh dày sừng ánh sáng chưa hẳn là ung thư, nó được xem là tổn thương giai đoạn tại chỗ ung thư da tế bào gai, nghĩa là các tổn thương được giới hạn tại chỗ và không xâm nhập tới các mô khác.
</p>
    </div>
    """, unsafe_allow_html=True)

    # Mụn do nội tiết tố hoạt động như thế nào?
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Những dấu hiệu và triệu chứng của bệnh dày sừng ánh sáng là gì?</p>
        <p style="font-size: 16px;">Bệnh dày sừng ánh sáng khởi đầu bằng lớp da cứng, dày, có vảy, kích thước như cục tẩy bút chì, có thể ngứa hoặc nóng rát ở vùng da bị ảnh hưởng. Theo thời gian, các tổn thương có thể biến mất, to lên, vẫn như cũ hoặc phát triển thành ung thư tế bào gai. Không có cách nào để bạn biết những tổn thương có thể trở thành ung thư hay không.</p>
        <p style="font-size: 16px; font-weight: bold; margin-top: 25px;">Các dấu hiệu và triệu chứng của bệnh dày sừng ánh sáng bao gồm:</p>
        <p style="font-size: 16px;"> - Mảng da thô, khô, cứng, đường kính nhỏ hơn 2.5 cm</p>
        <p style="font-size: 16px;"> - Mảng da từ bằng phẳng đến lồi lên hoặc sưng to trên da</p>
        <p style="font-size: 16px;"> - Bề mặt cứng giống như mụn cóc trong một số trường hợp</p>
        <p style="font-size: 16px;"> - Màu sắc đa dạng như màu hồng, đỏ hoặc nâu</p>
        <p style="font-size: 16px;"> - Ngứa hoặc nóng rát trong vùng da bị ảnh hưởng</p>
    </div>
    """, unsafe_allow_html=True)

    # Da dầu và vi khuẩn gây mụn
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Nguyên nhân nào gây ra bệnh dày sừng ánh sáng?</p>
        <p style="font-size: 16px;">Có nhiều nguyên nhân gây ra bệnh này, nhưng việc tiếp xúc lâu dài với ánh sáng mặt trời có thể coi là một trong những nguyên nhân phổ biến nhất gây ra tình trạng dày sừng ánh sáng. Bệnh thường gặp ở những người da trắng, mắt xanh ở từ 30 hoặc 40 tuổi trở lên.
Thỉnh thoảng, bệnh dày sừng ánh sáng có thể do việc tiếp xúc nhiều với tia X hoặc một số hóa chất công nghiệp gây ra.
</p>
    </div>
    """, unsafe_allow_html=True)

    # Các dạng mụn
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Những yếu tố nào làm tăng nguy cơ mắc bệnh dày sừng ánh sáng?</p>
        <p style="font-size: 16px; font-weight: bold; margin-top: 25px;">Bạn có nguy cơ cao mắc bệnh này nếu:</p>
        <p style="font-size: 16px;"> - Lớn hơn 60 tuổi</p>
        <p style="font-size: 16px;"> - Sống trong vùng khí hậu nhiều nắng</p>
        <p style="font-size: 16px;"> - Da trắng, mắt xanh</p>
        <p style="font-size: 16px;"> - Dễ bị cháy nắng</p>
        <p style="font-size: 16px;"> - Từng bị cháy nắng</p>
        <p style="font-size: 16px;"> - Thường xuyên tiếp xúc với ánh nắng mặt trời</p>
        <p style="font-size: 16px;"> - Nhiễm virus HPV</p>
        <p style="font-size: 16px;"> - Suy giảm hệ miễn dịch do hóa trị, bệnh bạch cầu, AIDS hoặc dùng thuốc ức chế thải ghép.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

if st.button("< BACK"):
        st.switch_page("pages/Home.py")