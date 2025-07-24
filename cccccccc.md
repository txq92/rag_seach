| Thành phần chính | Mô tả chức năng | Công nghệ/Kỹ thuật nổi bật | Tối ưu hóa liên quan |
|---|---|---|---|
| **Frontend (Web UI)** | Giao diện tương tác cho người dùng tải file/dán code và hiển thị báo cáo review. | React.js, Tailwind CSS, API FileReader | Giao diện thân thiện, hỗ trợ đa file. |
| **Backend (API Server)** | Điều phối luồng review, xử lý input (hỗ trợ đa file), tương tác với RAG/LLM, định dạng output. | Python (FastAPI/Flask) | Xử lý song song (concurrency) cho nhiều file, tiền lọc quy tắc đơn giản. |
| **RAG/LLM Core** | Bộ não hệ thống: chứa cơ sở dữ liệu vector, mô hình embedding và mô hình ngôn ngữ lớn (LLM). | ChromaDB (qua Docker), Embedding Model (Ollama), LLM (Ollama Phi4) | RAG cung cấp ngữ cảnh, LLM nhỏ gọn (Phi4), chất lượng dữ liệu RAG. |
| **Dữ liệu RAG: Codebase** | Lưu trữ cấu trúc và ngữ nghĩa của toàn bộ codebase để LLM tham chiếu. | AST (Abstract Syntax Tree), Chunking, Embedding | Phân tích AST giúp truy vấn chính xác, chunking tối ưu token. |
| **Dữ liệu RAG: Checklist** | Chứa các quy tắc review cụ thể dưới dạng JSON để LLM áp dụng. | File \*.json, Embedding | Quy tắc rõ ràng, không mâu thuẫn. |
| **Quy trình Review Input** | Nhận file code hoặc đoạn code cần review, phân tích AST và chia nhỏ (chunking). | FileReader (Frontend), AST parsing (Backend) | Xử lý từng file riêng lẻ rồi tổng hợp kết quả. |
| **Quy trình Truy vấn RAG** | Lấy về các quy tắc liên quan từ Checklist và các đoạn code mẫu từ Codebase. | Truy vấn ChromaDB (embedding similarity) | Đánh giá độ tương đồng để lấy thông tin liên quan nhất. |
| **Quy trình Xây dựng Prompt** | Tạo prompt rõ ràng, cấu trúc cho LLM với code input, quy tắc và ngữ cảnh. | Prompt Engineering | Prompt chặt chẽ giúp giảm ảo giác, tăng độ chính xác. |
| **Quy trình Output** | LLM trả về kết quả Markdown cho từng file/đoạn code, Backend tổng hợp lại. | Định dạng Markdown | Tổng hợp báo cáo Markdown chung cho nhiều file. |
| **Giảm thiểu Ảo giác** | Đảm bảo LLM chỉ sử dụng thông tin được cung cấp, không suy diễn. | Prompt Engineering, Chất lượng dữ liệu RAG, Ngưỡng tương đồng RAG | Các ràng buộc trong prompt, dữ liệu RAG chuẩn xác. |
