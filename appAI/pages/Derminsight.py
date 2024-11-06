import streamlit as st
import utils as utl
from pathlib import Path
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import base64
import streamlit.components.v1 as components


st.set_page_config(
    page_title="DERM INSIGHT APP",
    page_icon="🧊",
    layout="wide",
)
utl.local_css("streamlit.css")


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
logo_html = img_to_html('logo.png', width="100px", height="100px")  # Thay đường dẫn này bằng logo của bạn
right_image_html = img_to_html('anhbiamun.png', width="250px", height="230px")  # Thay đường dẫn bằng ảnh khác
bia_html1 = img_to_html('bia1.png', width="1306px", height="540px") 


css_code = """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .navbar a {
        text-decoration: none;
        color:  #FF8343;
        padding: 8px 16px;
        margin-top: 28px;
        font-size: 16px;
        font-weight: bold;
    }
    .navbar a:hover {
        color:  #FF8343;
        text-decoration: underline;
    }
    .logo {
        padding: 1px;
        margin-bottom: 50px;
    }
    .hero {
        background:  #FEEFDB;
        height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        color: black;
        margin-bottom: 80px;
        padding: 180px;
    }
    .hero h1 {
        font-size: 48px;
        margin-bottom: 20px;
    }
    .hero p {
        font-size: 18px;
        color: #6F514A;
    }
    .download-btn {
        background-color: #FF8343;
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 18px;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
        margin-left: 25px;
    }
    .download-btn:hover {
        background-color: linear-gradient(174.6deg, rgb(252, 200, 191) 11.8%, rgb(254, 159, 160) 89.9%);
    }
    </style>
"""

# Chèn CSS vào Streamlit
st.markdown(css_code, unsafe_allow_html=True)

# st.markdown("""
#     <script>
#     document.addEventListener('DOMContentLoaded', function() {
#         document.querySelector('.download-btn').onclick = function() {
#             window.location.href = "/?page=trainghiem";
#         };
#     });
#     </script>
# """, unsafe_allow_html=True)

# Thanh điều hướng và hero section
st.markdown(f"""
    <div class="navbar">
        <div class="logo">
            {logo_html}
        </div>
        <div>
            <a href="#home">Home</a>
            <a href="#about">Trải nghiệm Derm Insight</a>
            <a href="#services">About us</a>
            <a href="#projects">Vấn đề da liễu</a>
        </div>
    </div>

    <div class="hero" id="home">
        {bia_html1}
    </div>
""", unsafe_allow_html=True)
# <button class="download-btn" >THỬ NGAY</button>

st.markdown("""
    <style>
        .breadcrumb-nav {
            display: flex;
            margin-bottom: 1px;
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
            <a href="http://localhost:8501/Derminsight" class="current">Trải nghiệm Derm Insight</a>
            </li>
        </ol>
        </nav>

    """, unsafe_allow_html=True)


header_html = """
<h1 class="text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
    <span style="background: linear-gradient(to right, #ff6b3b, #ff914d); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 35px;">
        TRẢI NGHIỆM DERM INSIGHT
    </span>
</h1>
    """
st.markdown(header_html, unsafe_allow_html=True)


def img_to_base64(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

cachdung_base64 = img_to_base64('cachsudung.png')
cachdung_html = f'<img src="data:image/png;base64,{cachdung_base64}" style="width:100%; height:auto; border-radius: 5px;"/>'

st.markdown(f"""
    <div style="background-color: #f4f4f4; padding: 35px 60px; border-radius: 8px; text-align: center; max-width: 700px; margin: 0 auto; margin-bottom: 55px;">
        <h2 style="font-size: 25px;font-weight: bold; color:  #ed5b2d; margin-bottom: 20px;">Cách sử dụng DERM INSIGHT</h2>
        <div style="width: 100%; height: 89%; border-radius: 8px;">
        {cachdung_html}
        </div>
    </div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_trained_model():
        model = load_model('ResNet152_26102024.h5')  # Thay thế bằng đường dẫn đến mô hình của bạn
        return model

    # Function to preprocess the image
def preprocess_image(image):
        # Resize image to (256, 192) as required by your model
        image = np.array(image)
        image = cv2.resize(image, (256, 192))  # Chú ý đổi thứ tự kích thước
        image = image / 255.0  # Normalize to [0, 1]
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        return image

    # Function to predict skin disease
def predict_image(image, model, threshold=0.5):
        processed_image = preprocess_image(image)
        
        # Make prediction using the model
        predictions = model.predict(processed_image)
        
        # Assuming the model outputs probabilities for 4 classes
        classes = ['ak', 'av', 'ez', 'ps', 'unknown']
        
        predicted_class = np.argmax(predictions, axis=1)
        max_probability = np.max(predictions)  # Lấy xác suất cao nhất
        
        # Nếu xác suất cao nhất dưới ngưỡng, trả về "unknown"
        if max_probability < threshold:
            return 'unknown', predictions
        else:
            return classes[predicted_class[0]], predictions


st.subheader("Hãy tải hình ảnh của bạn")
st.write("*Lưu ý:*")
st.write("1. Hãy chụp trong điều kiện ánh sáng tốt")
st.write("2. Tránh ánh sáng quá mạnh hoặc quá tối để không ảnh hưởng đến kết quả phân tích da của bạn")
st.write("3. Đảm bảo hình ảnh được hiển thị rõ ràng và không bị che khuất")


    # Function to display results after prediction
def Hoantat():
        st.divider()
        header_html = """
        <h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
            <span style="background: linear-gradient(to right, #ff7e5f, #feb47b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 35px;">KẾT QUẢ</span>
        """
        st.markdown(header_html, unsafe_allow_html=True)
        
        # Load model and make prediction
        model = load_trained_model()
        prediction, predictions = predict_image(image, model)
        

        with st.container():
            col1, col2, col3 = st.columns([0.4, 0.1, 0.5])

            with col1:
                st.image(image, use_column_width=True)

            with col2:
                st.write("")
            
            with col3:
                st.subheader("Tình trạng da")
                if prediction == 'unknown':
                    st.write("Không phát hiện vùng bệnh cần chẩn đoán.")
                else:
                    # st.write("- Prediction: **[{}]({})**".format(prediction.upper(), prediction))
                    # st.write("Xác suất dự đoán: ", predictions)
                    if prediction == 'av':  # Nếu dự đoán là "av"
                        
                        # Hiển thị thông tin bệnh
                        st.write("- Kết quả dự đoán:")

                        ketquabenh = """ 
                            <p style="font-size: 22px;font-weight: bold; color: #e65410; margin-left: 30px;">Mụn trứng cá nặng (Acne Vulgaris)</p>
                        """
                        st.markdown(ketquabenh, unsafe_allow_html=True)
                        st.write("")
                        with st.popover("TÌM HIỂU NGAY"):
                            st.write("")
                            st.markdown(
                            """ 
                            <p style="font-size: 25px; color: #e65410; font-weight: bold; margin-bottom: 13px">BẠN CÓ BIẾT ⁉️</p>
                            <p style="font-size: 16px; margin-bottom: 10px">Mụn trứng cá nặng, hay còn gọi là Acne Vulgaris, là một tình trạng da phổ biến, thường xuất hiện trong tuổi dậy thì nhưng cũng có thể xảy ra ở người lớn. Đây là một dạng mụn trứng cá nghiêm trọng, thường gây ra các nốt mụn lớn, sưng đỏ và đau đớn. Mụn trứng cá nặng có thể để lại sẹo và các dấu hiệu trên da, ảnh hưởng đến tâm lý và chất lượng cuộc sống của người mắc phải.</p>
                            <a class="Link" href="http://localhost:8501/muntrungca" style="font-size: 16px;">THÔNG TIN CHI TIẾT 🫵🏻</a>
                            """
                            , unsafe_allow_html=True)

                            st.write("")
                            st.write("")


                        st.write("")
                        st.subheader("Lời khuyên")
                        st.write("- Điều trị mụn bằng Benzoyl Peroxide, Salicylic Acid, Retinoids, Acid Azelaic, và Niacinamide.")
                        st.write("- Đi khám bác sĩ nếu mụn nặng, lan rộng hoặc không cải thiện sau 3-4 tháng tự điều trị.")
                        st.write("- Chăm sóc da: rửa mặt đúng cách, dưỡng ẩm, dùng kem chống nắng, tránh sờ mặt.")
                        st.write("- Thay đổi chế độ ăn uống, giảm đường, dầu mỡ, sữa động vật.")
                    
                    elif prediction == 'ak':  # Dày sừng quang hóa (Actinic Keratosis)
                        st.write("- Kết quả dự đoán:")

                        ketquabenh = """ 
                            <p style="font-size: 22px;font-weight: bold; color: #e65410; margin-left: 30px;">Dày sừng quang hóa (Actinic Keratosis)</p>
                        """
                        st.markdown(ketquabenh, unsafe_allow_html=True)
                        st.write("")

                        with st.popover("TÌM HIỂU NGAY"):
                            st.write("")
                            st.markdown(
                            """ 
                            <p style="font-size: 25px; color: #e65410; font-weight: bold; margin-bottom: 13px">BẠN CÓ BIẾT ⁉️</p>
                            <p style="font-size: 16px; margin-bottom: 10px">Actinic Keratosis là một bệnh ngoài da phổ biến ảnh hưởng đến nhiều người. Nó phát sinh do da tiếp xúc kéo dài với ánh sáng mặt trời hoặc tia cực tím. Các mảng hoặc tổn thương thô ráp có vảy trên da là đặc điểm của tổn thương của bệnh. Các yếu tố dễ bị tổn thương thường được coi là triệu chứng tiền ung thư. Nếu không được phát hiện sớm và điều trị kịp thời có thể dẫn đến ung thư da tế bào vảy.</p>
                            <a class="Link" href="http://localhost:8501/benhdaysung" style="font-size: 16px;">THÔNG TIN CHI TIẾT 🫵🏻</a>
                            """
                            , unsafe_allow_html=True)

                            st.write("")
                            st.write("")

                        st.write("")
                        st.subheader("Lời khuyên")
                        st.write("- Sử dụng thuốc mỡ chứa Fluorouracil hoặc Imiquimod theo chỉ định của bác sĩ.")
                        st.write("- Tránh tiếp xúc ánh nắng mặt trời và dùng kem chống nắng có chỉ số SPF cao.")
                        st.write("- Khám bác sĩ để theo dõi và điều trị sớm nếu có biến đổi bất thường trên da.")
                    
                    elif prediction == 'ez':  # Chàm (Eczema)
                        st.write("- Kết quả dự đoán:")

                        ketquabenh = """ 
                            <p style="font-size: 20px;font-weight: bold; color: #e65410; margin-left: 30px;">Chàm (Eczema)</p>
                        """
                        st.markdown(ketquabenh, unsafe_allow_html=True)
                        st.write("")

                        with st.popover("TÌM HIỂU NGAY"):
                            st.write("")
                            st.markdown(
                            """ 
                            <p style="font-size: 25px; color: #e65410; font-weight: bold; margin-bottom: 13px">BẠN CÓ BIẾT ⁉️</p>
                            <p style="font-size: 16px; margin-bottom: 10px">Bệnh chàm là tên chung của một nhóm bệnh viêm da đặc trưng bởi da khô, bong vảy, ngứa, phồng rộp, phát ban và nhiễm trùng. Ngứa da là biểu hiện phổ biến nhất của bệnh chàm. Có bảy loại bệnh chàm: viêm da dị ứng, viêm da tiếp xúc, chàm tổ đỉa, chàm đồng tiền, viêm da tiết bã và viêm da ứ đọng. Nếu bệnh chàm không được điều trị kịp thời sẽ dễ phát triển thành các đợt bùng phát nặng kèm theo các biến chứng nguy hiểm khác kéo dài nhiều ngày hoặc nhiều tuần. Đôi khi, bệnh chàm dễ bị nhầm lẫn với các bệnh ngoài da khác có triệu chứng tương tự bệnh vẩy nến.</p>
                            <a class="Link" href="http://localhost:8501/benhcham" style="font-size: 16px;">THÔNG TIN CHI TIẾT 🫵🏻</a>
                            """
                            , unsafe_allow_html=True)

                            st.write("")
                            st.write("")

                        st.write("")
                        st.subheader("Lời khuyên")
                        st.write("- Sử dụng kem dưỡng ẩm hàng ngày, đặc biệt là sau khi tắm.")
                        st.write("- Tránh sử dụng các sản phẩm gây kích ứng và nước nóng.")
                        st.write("- Nếu ngứa hoặc viêm, có thể sử dụng kem corticosteroid theo hướng dẫn bác sĩ.")
                    
                    elif prediction == 'ps':  # Vẩy nến (Psoriasis)
                        st.write("- Kết quả dự đoán:")

                        ketquabenh = """ 
                            <p style="font-size: 20px;font-weight: bold; color: #e65410; margin-left: 30px;">Vẩy nến (Psoriasis)</p>
                        """
                        st.markdown(ketquabenh, unsafe_allow_html=True)
                        st.write("")

                        with st.popover("TÌM HIỂU NGAY"):
                            st.write("")
                            st.markdown(
                            """ 
                            <p style="font-size: 25px; color: #e65410; font-weight: bold; margin-bottom: 13px">BẠN CÓ BIẾT ⁉️</p>
                            <p style="font-size: 16px; margin-bottom: 10px">Bệnh vẩy nến là một bệnh viêm da mãn tính không rõ nguồn gốc hoặc không rõ nguồn gốc. Các nhà khoa học cho rằng nó liên quan đến yếu tố môi trường và di truyền. Hệ thống miễn dịch hoạt động quá mức khiến tế bào tăng sinh nhanh chóng, dẫn đến hình thành các mảng vảy. Hệ thống miễn dịch của cơ thể hoạt động quá mức, khiến tế bào nhân lên nhanh chóng và hình thành vảy. Các đặc điểm cơ bản của bệnh vẩy nến bao gồm da có vảy và viêm da. Bệnh xảy ra ở hầu hết các bộ phận trên cơ thể nhưng thường gặp ở da đầu, khuỷu tay và đầu gối.</p>
                            <a class="Link" href="http://localhost:8501/benhvaynen" style="font-size: 16px;">THÔNG TIN CHI TIẾT 🫵🏻</a>
                            """
                            ,unsafe_allow_html=True)

                            st.write("")
                            st.write("")

                        st.write("")
                        st.subheader("Lời khuyên")
                        st.write("- Sử dụng kem dưỡng ẩm và thuốc chứa Salicylic Acid hoặc corticosteroid.")
                        st.write("- Tránh căng thẳng, bảo vệ da khỏi tổn thương và duy trì lối sống lành mạnh.")
                        st.write("- Tham khảo bác sĩ da liễu để có phương pháp điều trị phù hợp nếu tình trạng trở nặng.")
                    else:
                        st.write("Không có khuyến nghị cụ thể cho tình trạng da của bạn.")
        st.write("")
        button_back = st.button("QUAY LẠI", type="primary")
        if button_back:
            st.session_state.page = "main"
            
        # if st.button("Phân tích ảnh khác"):
        #     st.session_state.clear()  # Xóa tất cả dữ liệu trong session state
        #     trainghiem()  
        #     st.session_state.page = "trainghiem"


    # Hàm tính độ sắc nét của ảnh sử dụng biến đổi Laplacian
def calculate_image_sharpness(image):
        # Chuyển ảnh từ PIL sang OpenCV
        image_cv = np.array(image.convert('L'))  # Chuyển sang ảnh xám (grayscale)
        
        # Tính biến đổi Laplacian
        laplacian = cv2.Laplacian(image_cv, cv2.CV_64F)
        
        # Tính độ sắc nét dựa trên phương sai của Laplacian
        sharpness = laplacian.var()
        
        return sharpness

    # Hàm kiểm tra chất lượng ảnh dựa trên độ sắc nét
def check_image_quality(image, threshold=100):
        sharpness = calculate_image_sharpness(image)
        
        # Kiểm tra nếu độ sắc nét vượt qua ngưỡng cho trước
        if sharpness >= threshold:
            return True
        return False

st.write("")
uploaded_file = st.file_uploader("Chọn ảnh", type=["png", "jpg", "jpeg"])


if uploaded_file is not None:
        col1, col2, col3= st.columns([0.2,0.6,0.2])
        with col1:
            st.write("")
        with col2:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, use_column_width=True) 

        with col3:
            st.write("")
    
        if check_image_quality(image):
            st.markdown(
                """
             <div style="
                border: 1px solid rgba(255, 165, 0, 0.46);
                background-color: rgba(255, 165, 0, 0.12);
                box-shadow: 0px 0px 2px #FFA500;
                color: #FF8C00;
                padding: 10px;
                border-radius: 5px;
                font-family: 'Montserrat', sans-serif;
                font-size: 16px;
                font-weight: light;
                text-align: left;
                width: 60%;
                margin: 0 auto;
                margin-bottom: 10px;
            ">
                <i class="far fa-check-circle" style="margin-right: 5px; color: #FFA500;"></i>
                <strong>Ảnh tải lên rõ nét</strong> !
            </div>
                """, 
                unsafe_allow_html=True
            )
            
            button_hoantat = st.button("HOÀN TẤT", type="primary")
            if button_hoantat:
                Hoantat()
        else:
            st.markdown(
                """
                <div style="
                    border: 1px solid rgba(241, 6, 6, 0.81);
                    background-color: rgba(220, 17, 1, 0.16);
                    box-shadow: 0px 0px 2px #ff0303;
                    color: #ff0303;
                    padding: 10px;
                    border-radius: 5px;
                    font-family: 'Montserrat', sans-serif;
                    font-size: 16px;
                    font-weight: light;
                    text-align: center;
                    width: 60%;
                    margin: 0 auto;
                    margin-bottom: 10px;
                ">
                    <i class="far fa-times-circle" style="margin-right: 5px; color: #ff0303;"></i>
                    <strong>Ảnh chưa đủ rõ nét.</strong> Vui lòng tải lại ảnh sắc nét hơn
                </div>
                """, 
                unsafe_allow_html=True
            )

st.write("")
st.write("")
if st.button("< BACK"):
        st.switch_page("pages/Home.py")



# # CSS cho phần footer
# footer_css = """
#     <style>
#     .footer {
#         background-color: white;  
#         color: white;
#         padding: 1px ;
#         text-align: center;
#     }
#     .footer .container {
#         display: flex;
#         flex-direction: column;
#         justify-content: center;
#         align-items: center;
#     }
#     .footer-icons a {
#         margin-top: 1px;
#         margin-bottom: 10px;
#         color: #FF8343;
#         padding: 3px;  /* Giảm kích thước padding để icon nhỏ hơn */
#         border-radius: 50%;
#         font-size: 17px;  /* Giảm font-size để icon nhỏ hơn */
#         display: inline-block;
#         text-decoration: none;
#     }
#     .footer-icons a:hover {
#         color: #343a40;  /* Màu khi hover */
#     }
#     .footer-bottom {
#         background-color: #FFEADF;
#         padding: 10px;
#         width: 100%;
#         text-align: center;
#         font-size: 14px;
#         color: #503C37;;
#         font-weight: bold;
#     }
#     .footer-bottom a {
#         color: #503C37;
#         text-decoration: none;
#     }
#     </style>
# """

# # Thêm CSS vào ứng dụng
# st.markdown(footer_css, unsafe_allow_html=True)

# # HTML cho footer
# footer_html = """
# <div class="footer">
#     <div class="footer-bottom">
#         © 2024 Copyright:
#         <a>Derminsight.team@gmail.com</a>
#     </div>
#     <div class="container">
#         <div class="footer-icons">
#             <a href="#!" role="button"><i class="fab fa-facebook-f"></i></a>
#             <a href="#!" role="button"><i class="fab fa-twitter"></i></a>
#             <a href="#!" role="button"><i class="fab fa-google"></i></a>
#             <a href="#!" role="button"><i class="fab fa-instagram"></i></a>
#             <a href="#!" role="button"><i class="fab fa-linkedin-in"></i></a>
#             <a href="#!" role="button"><i class="fab fa-github"></i></a>
#         </div>
#     </div>
# </div>
# """

# # Thêm HTML vào ứng dụng
# st.markdown(footer_html, unsafe_allow_html=True)

# # Thêm link tới Font Awesome để hiển thị icon
# st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"/>', unsafe_allow_html=True)


footer_css = """
    <style>
    .footer {
        background-color: #FF8343;  /* Màu nền cam */
        color: white;
        padding: 10px;
        text-align: center;
    }
    .footer .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .footer-icons a {
        margin: 5px;
        color: black;
        border: 1px solid white;
        padding: 8px;  /* Giảm kích thước padding để icon nhỏ hơn */
        border-radius: 50%;
        font-size: 16px;  /* Giảm font-size để icon nhỏ hơn */
        display: inline-block;
        text-decoration: none;
    }
    .footer-icons a:hover {
        color: #343a40;  /* Màu khi hover */
    }
"""

# Thêm CSS vào ứng dụng
st.markdown(footer_css, unsafe_allow_html=True)




# # Thêm phần Footer
# st.markdown("""
# <style>
# @import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400);
# body {
#   font-family: 'Source Sans Pro', sans-serif;
#   font-weight: 300;
#   background-color: lightblue;
#   color: white;
# }
# .footer #button { 
#   width: 35px;
#   height: 35px;
#   border: #FF8343 12px solid;
#   border-radius: 35px;
#   margin: 0 auto;
#   position: relative;
#   transition: all 1s ease;
# }
# .footer #button:hover {
#   border: #3A3A3A 12px solid;
# }
# .footer {
#   bottom: 0;
#   left: 0;
#   position: fixed;
#   width: 100%;
#   height: 100px;
#   overflow: hidden;
#   margin: 0 auto;
#   transition: all 1s ease;
#   z-index: 999;
# }
# .footer:hover {
#   height: 100px;
# }
# .footer #container {
#   margin-top: 5px;
#   width: 100%;
#   height: 100%;
#   position: relative;
#   top: 0;
#   left: 0;
#   background: #FF8343;
# }
# .footer #cont {
#   position: relative;
#   top: -60px;
#   right: 190px;
#   width: 150px;
#   height: auto;
#   margin: 0 auto;
# }
# .footer_center {
#   width: 500px;
#   float: left;
#   text-align: center;
# }
# .footer h3 {
#   font-family: 'Helvetica';
#   font-size: 30px;
#   font-weight: bold;
#   margin-top: 70px;
#     color: white;
#   margin-left: 40px;
# }
# </style>

# <div class="footer">
#   <div id="button"></div>
#   <div id="container">
#     <div id="cont">
#       <div class="footer_center">
#         <h3>WELCOME TO DERM INSIGHT</h3>
#       </div>
#     </div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

def img_to_html(img_path, width="00px", height="80px"):
    img_html = f"<img src='data:image/png;base64,{img_to_bytes(img_path)}' style='width:{width}; height:{height};'>"
    return img_html

# Sử dụng hàm img_to_html để mã hóa logo và hình ảnh bên phải
logo_html = img_to_html('logo.png', width="200px", height="200px")  # Thay đường dẫn này bằng logo của bạn


# Phần CSS
css_code = """
    <style>
    .footer {
        background-color: #f8f9fa;
        padding: 25px ;
        border-top: 1px solid #e9ecef;
        font-family: 'Arial', sans-serif;
    
    }
    .footer h4 {
        margin-left: 40x;
        font-size: 18px;
        color: #6c757d;

    }
    .footer .fix {
        margin-left: 60px;
        font-size: 18px;
        color: #6c757d;

    }

    .footer p, .footer address, .footer a {
        color: #6c757d;
        text-decoration: none;
        font-size: 16px;
        margin-right: 20px;
    }
    .footer a:hover {
        color:  #FF8343;
        text-decoration: underline;
    }
    .footer .widget-section {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        justify-content: space-between;
    }
    .footer .widget-section div {
        flex: 1;
        max-width: 600px;
    }
  
    .footer form input[type="email"] {
        width: 100%;
        padding: 0.5rem;
        margin-top: 10px;
        margin-bottom: 15px;
        border: 1px solid #ced4da;
        border-radius: 4px;
    }
    .footer form button {
        width: 100%;
        padding: 0.5rem;
        background-color: #FF8343;
        color: #fff;
        border: none;
        border-radius: 4px;
    }
     .footer-bottom {
        background-color: rgba(0, 0, 0, 0.2);
        padding: 15px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: white;
        font-weight: bold;
        margin: 5px;
    
    }
    .footer-bottom a {
        color: #6c757d;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
"""

# Chèn CSS vào Streamlit
st.markdown(css_code, unsafe_allow_html=True)

# Phần HTML
st.markdown(f"""
<footer class="footer">
  <section class="widget-section">
    <div >
      {logo_html}
    </div>
    <div>
      <h4>Get in Touch</h4>
      <address> 232/6 Vo Thi Sau Street, Ward 7, District 3, Ho Chi Minh City, Vietnam</address>
      <p><a href="tel:+84123456789">0123 456 789</a></p>
      <p><a href="mailto:derminsight.team@gmail.com">derminsight.team@gmail.com</a></p>
    </div>
    <div>
      <h4 class="fix">Learn More</h4>
      <ul style="list-style-type: none; padding-left: 0;">
        <li><a href="#!">About</a></li>
        <li><a href="#!">Contact</a></li>
        <li><a href="#!">Advertise</a></li>
        <li><a href="#!">Terms of Service</a></li>
        <li><a href="#!">Privacy Policy</a></li>
      </ul>
    </div>
    <div>
      <h4>Our Newsletter</h4>
      <p>Subscribe to our newsletter to get our news & discounts delivered to you.</p>
      <form action="#!">
        <input type="email" placeholder="Email Address" required>
        <button type="submit">Subscribe</button>
      </form>
    </div>
  </section>
  <div class="container">
        <div class="footer-icons">
            <a href="#!" role="button"><i class="fab fa-facebook-f"></i></a>
            <a href="#!" role="button"><i class="fab fa-twitter"></i></a>
            <a href="#!" role="button"><i class="fab fa-google"></i></a>
            <a href="#!" role="button"><i class="fab fa-instagram"></i></a>
            <a href="#!" role="button"><i class="fab fa-linkedin-in"></i></a>
            <a href="#!" role="button"><i class="fab fa-github"></i></a>
        </div>
    </div>
    <div class="footer-bottom">
        © 2024 Copyright:
        <a>derminsight.team@gmail.com</a>
    </div>
</footer>
"""
,unsafe_allow_html=True)

