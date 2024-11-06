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
    page_title="KHÁM PHÁ BỆNH CHÀM",
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
anhbia = img_to_html('biabenhcham.jpg', width="1600px", height="350px")
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
            <a href="#" class="current">Bệnh chàm</a>
            </li>
        </ol>
        </nav>

    """, unsafe_allow_html=True)

# Header with orange gradient text
header_html = """
<h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
    TẤT CẢ VỀ <span style="background: linear-gradient(to right, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 35px;">BỆNH CHÀM (EZ) </span> 
</h1>
<p class="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">
    Bệnh chàm là tên chung của một nhóm bệnh viêm da đặc trưng bởi da khô, bong vảy, ngứa, phồng rộp, phát ban và nhiễm trùng. Ngứa da là biểu hiện phổ biến nhất của bệnh chàm. Có bảy loại bệnh chàm: viêm da dị ứng, viêm da tiếp xúc, chàm tổ đỉa, chàm đồng tiền, viêm da tiết bã và viêm da ứ đọng. Nếu bệnh chàm không được điều trị kịp thời sẽ dễ phát triển thành các đợt bùng phát nặng kèm theo các biến chứng nguy hiểm khác kéo dài nhiều ngày hoặc nhiều tuần. Đôi khi, bệnh chàm dễ bị nhầm lẫn với các bệnh ngoài da khác có triệu chứng tương tự bệnh vẩy nến.
"""

# Displaying the header in Streamlit
st.markdown(header_html, unsafe_allow_html=True)


# Tiêu đề phụ
st.markdown("""
    <p style="font-size: 24px; color: #FF8343; font-weight: bold; margin-top: 20px;">
        Lời khuyên cho bệnh chàm:
    </p>
""", unsafe_allow_html=True)

# Nội dung mô tả với các gạch đầu dòng
st.markdown("""
    <ul style="font-size: 18px; line-height: 1.6;">
        <li>Dưỡng ẩm da thường xuyên để ngăn ngừa khô da.</li>
        <li>Tránh các yếu tố kích thích như hóa chất, xà phòng mạnh, và chất gây dị ứng.</li>
        <li>Sử dụng sản phẩm dịu nhẹ, không chứa hương liệu.</li>
        <li>Giữ da sạch và khô nhưng không rửa quá nhiều.</li>
        <li>Hạn chế gãi để tránh làm tổn thương da.</li>
        <li>Thăm khám bác sĩ để nhận thuốc bôi hoặc uống nếu tình trạng nặng.</li>
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
        <div style="font-size: 16px; ">Bệnh chàm là gì?</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">2</div>
        <div style="font-size: 16px;">Triệu chứng mắc bệnh chàm</div>
    </div>
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <div style="font-size: 36px; color: orange; font-weight: bold; margin-right: 10px;">3</div>
        <div style="font-size: 16px;">Cách điều trị bệnh chàm</div>
    </div>
    """, unsafe_allow_html=True)
# Right column with detailed content for each heading
with col2:
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Bệnh chàm là gì?</p>
        <p style="font-size: 16px;">Chàm là tình trạng khiến da bạn trở nên khô, ngứa và sần sùi. Tình trạng này làm suy yếu chức năng hàng rào bảo vệ da, có nhiệm vụ giúp da giữ độ ẩm và bảo vệ cơ thể bạn khỏi các yếu tố bên ngoài. Bệnh chàm có thể ảnh hưởng đến bất kỳ ai ở mọi lứa tuổi. Các triệu chứng thường xuất hiện trong thời thơ ấu và kéo dài đến tuổi trưởng thành. Trẻ sơ sinh dễ bị bệnh chàm, khoảng 10% đến 20% sẽ mắc bệnh này. Tuy nhiên, gần một nửa số trẻ sơ sinh được chẩn đoán mắc bệnh chàm sẽ hết bệnh hoặc có sự cải thiện đáng kể khi lớn lên.
</p>
    </div>
    """, unsafe_allow_html=True)

    # Mụn do nội tiết tố hoạt động như thế nào?
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Triệu chứng mắc bệnh chàm</p>
        <p style="font-size: 16px;">Với mỗi người, biểu hiện bệnh chàm sẽ khác nhau. Các đợt bùng phát không phải lúc nào cũng xảy ra trong cùng một khu vực. Triệu chứng đặc trưng của bệnh chàm là ngứa, đôi khi biểu hiện ngứa xuất hiện trước khi phát ban. Những biểu hiện khác của bệnh chàm cũng có thể xuất hiện như: Đỏ, khô, nứt, dày da. Bệnh chàm có thể xuất hiện ở bất cứ vùng da nào trên cơ thể.</p>
        <p style="font-size: 16px; font-weight: bold; margin-top: 25px;">Triệu chứng ở trẻ sơ sinh</p>
        <p style="font-size: 16px;">Ở trẻ sơ sinh, phát ban ngứa có thể dẫn đến tình trạng chảy nước, đóng vảy, chủ yếu ở mặt, nếp da (kẽ da) và da đầu. Biểu hiện cũng có thể xuất hiện trên cánh tay, chân, lưng và ngực của trẻ.</p>
        <p style="font-size: 16px; font-weight: bold; margin-top: 25px;">Triệu chứng ở trẻ nhỏ </p>
        <p style="font-size: 16px;">Trẻ em và thanh thiếu niên khi mắc bệnh thường bị phát ban ở những vị trí như khuỷu tay, sau đầu gối, trên cổ/trên cổ tay, mắt cá chân. Phát ban chuyển thành vảy và khô.</p>
        <p style="font-size: 16px; font-weight: bold; margin-top: 25px;">Triệu chứng ở người lớn  </p>
        <p style="font-size: 16px;">Tình trạng phát ban thường xảy ra trên mặt, mặt sau của đầu gối, cổ tay, bàn tay hoặc bàn chân. Da có thể xuất hiện tình trạng rất khô, dày hoặc có vảy. Ở những người da trắng, những vùng da này có thể bắt đầu hơi đỏ và sau đó chuyển sang màu nâu. Ở những người da sẫm màu, bệnh chàm có thể ảnh hưởng đến các sắc tố da, làm cho vùng bị ảnh hưởng sáng hơn hoặc sẫm màu hơn.</p>
              
       
    </div>
    """, unsafe_allow_html=True)

    # Da dầu và vi khuẩn gây mụn
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <p style="font-size: 24px; color: #FF8343; font-weight: bold;">Cách điều trị bệnh chàm</p>
        <p style="font-size: 16px;"> - Sử dụng kem/thuốc mỡ/sáp dưỡng ẩm làm dịu tình trạng viêm và duy trì độ ẩm cho da, giúp da mau lành</p>
        <p style="font-size: 16px;"> - Kem hydrocortisone và thuốc kháng histamin giúp giảm mẩn đỏ, ngứa và sưng tấy. Bạn chỉ nên thoa hydrocortisone lên các phần da bị chàm 4 lần/ngày trong 7 ngày. Tránh xa mắt, trực tràng và bộ phận sinh dục. Lưu ý, hỏi ý kiến bác sĩ nếu đang mang thai hoặc cho con bú.</p>
        <p style="font-size: 16px;"> - Đắp gạc ướt.</p>
        <p style="font-size: 16px;"> - Thư giãn và tập thiền.</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("< BACK"):
        st.switch_page("pages/Home.py")