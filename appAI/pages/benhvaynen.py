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
    page_title="KHÁM PHÁ BỆNH VẨY NẾN",
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
anhbia = img_to_html('biavaynen.jpg', width="1600px", height="350px")
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
            <a href="#" class="current">Bệnh vẩy nến</a>
            </li>
        </ol>
        </nav>

    """, unsafe_allow_html=True)

# Header with orange gradient text
header_html = """
<h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
    TẤT CẢ VỀ <span style="background: linear-gradient(to right, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 35px;">BỆNH VẨY NẾN (PS) </span>
</h1>
<p class="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">
    Bệnh vẩy nến là một bệnh viêm da mãn tính không rõ nguồn gốc hoặc không rõ nguồn gốc. Các nhà khoa học cho rằng nó liên quan đến yếu tố môi trường và di truyền. Hệ thống miễn dịch hoạt động quá mức khiến tế bào tăng sinh nhanh chóng, dẫn đến hình thành các mảng vảy. Hệ thống miễn dịch của cơ thể hoạt động quá mức, khiến tế bào nhân lên nhanh chóng và hình thành vảy. Các đặc điểm cơ bản của bệnh vẩy nến bao gồm da có vảy và viêm da. Bệnh xảy ra ở hầu hết các bộ phận trên cơ thể nhưng thường gặp ở da đầu, khuỷu tay và đầu gối.
</p>
"""

# Displaying the header in Streamlit
st.markdown(header_html, unsafe_allow_html=True)

# Tiêu đề phụ
st.markdown("""
    <p style="font-size: 24px; color: #FF8343; font-weight: bold; margin-top: 20px;">
        Lời khuyên cho bệnh vẩy nến:
    </p>
""", unsafe_allow_html=True)

# Nội dung mô tả với các gạch đầu dòng
st.markdown("""
    <ul style="font-size: 18px; line-height: 1.6;">
        <li>Dưỡng ẩm da đều đặn để giảm khô và ngứa.</li>
        <li>Tránh các yếu tố kích thích như stress, chấn thương da, và nhiễm trùng.</li>
        <li>Tắm nước ấm với muối Epsom hoặc yến mạch để làm dịu da.</li>
        <li>Áp dụng liệu pháp ánh sáng nếu được khuyến cáo.</li>
        <li>Sử dụng thuốc theo chỉ định bác sĩ, bao gồm kem bôi hoặc thuốc uống.</li>
        <li>Giữ lối sống lành mạnh với chế độ ăn cân bằng và đủ giấc ngủ.</li>
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
        <div style="font-size: 16px; ">Bệnh vảy nến là gì?</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">2</div>
        <div style="font-size: 16px;">Dấu hiệu mắc bệnh vảy nến</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">3</div>
        <div style="font-size: 16px;">Nguyên nhân nào gây ra bệnh vảy nến?</div>
    </div>

    """, unsafe_allow_html=True)
# Right column with detailed content for each heading
with col2:
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Bệnh vảy nến là gì?</p>
        <p style="font-size: 16px;">Vảy nến là các mảng da bong tróc tạo thành vảy. Vị trí tổn thương có màu hồng hoặc đỏ, thậm chí màu tím hoặc nâu sẫm; riêng vảy có thể màu xám, màu trắng hoặc bạc. Những mảng này có thể xuất hiện bất kỳ vị trí nào trên cơ thể, thường gặp ở khuỷu tay, đầu gối, da đầu và lưng dưới.
</p>
        <p style="font-size: 16px;">Bệnh vảy nến là bệnh mạn tính (kéo dài) không lây, có thể gặp mọi lứa tuổi nhưng thường xuất hiện ở người lớn từ 20 – 30 tuổi và từ 50 – 60 tuổi, tỷ lệ nam và nữ tương đương nhau. Hầu hết, người bệnh vảy nến chỉ bị ảnh hưởng bởi các mảng nhỏ trên da nhưng một số trường hợp, các mảng vảy nến có thể ngứa hoặc đau.
</p>
    </div>
    """, unsafe_allow_html=True)

    # Mụn do nội tiết tố hoạt động như thế nào?
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Dấu hiệu mắc bệnh vảy nến</p>
        <p style="font-size: 16px;">Bệnh vảy nến bao gồm các giai đoạn không triệu chứng hoặc triệu chứng nhẹ, sau đó đến giai đoạn triệu chứng nghiêm trọng hơn.</p>
        <p style="font-size: 16px; font-weight: bold; margin-top: 25px;">Các dấu hiệu và triệu chứng phổ biến của bệnh vảy nến bao gồm:</p>
        <p style="font-size: 16px;"> - Phát ban loang lổ với nhiều hình dạng khác nhau, từ những nốt vảy giống như vảy gàu đến nốt ban lớn khắp cơ thể.</p>
        <p style="font-size: 16px;"> - Ban có màu khác nhau. Người có màu da nâu hoặc da đen thường rơi vào sắc tím. Người da trắng có sắc hồng hoặc đỏ với vảy bạc.</p>
        <p style="font-size: 16px;"> - Đốm vảy nhỏ (thường gặp ở trẻ em).</p>
        <p style="font-size: 16px;"> - Da khô, nứt nẻ có thể chảy máu.</p>
        <p style="font-size: 16px;"> - Ngứa, rát hoặc đau nhức.</p>
    </div>
    """, unsafe_allow_html=True)

    # Da dầu và vi khuẩn gây mụn
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Nguyên nhân nào gây ra bệnh vảy nến?</p>
        <p style="font-size: 16px;">Bệnh vảy nến xảy ra khi các tế bào da được thay thế nhanh hơn bình thường. Thông thường, các tế bào da được tạo ra và thay thế sau mỗi 3 – 4 tuần nhưng quá trình này chỉ mất khoảng 3 – 7 ngày ở bệnh nhân vảy nến.  Từ đó khiến cơ thể người bệnh gia tăng sản xuất tế bào da, dẫn đến sự tích tụ các tế bào da tạo ra các mảng các mảng bong tróc, sần sùi phủ đầy vảy.</p>
        <p style="font-size: 16px;">Các nhà khoa học ghi nhận người bị bệnh vảy nến gặp rối loạn về hệ thống miễn dịch. Hệ thống miễn dịch là cơ chế phòng vệ của cơ thể giúp chống lại bệnh tật và nhiễm trùng nhưng lại tấn công nhầm các tế bào da khỏe mạnh ở người bị bệnh vảy nến.</p>
        <p style="font-size: 16px;">Bệnh vảy nến có thể di truyền trong gia đình. Khoảng 1/3  người mắc bệnh vảy nến báo cáo có tiền sử gia đình mắc bệnh. Các nghiên cứu về cặp song sinh giống hệt nhau cho thấy 70% khả năng một cặp song sinh mắc bệnh nếu người kia mắc chứng rối loạn này; tỷ lệ này chiếm 20% ở cặp song sinh không giống hệt nhau. Những phát hiện này cho thấy cả tính nhạy cảm di truyền và phản ứng môi trường trong việc phát triển bệnh vẩy nến.</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("< BACK"):
        st.switch_page("pages/Home.py")