# I. Redis
- Inmemory-Database (Nhanh hơn Disk-DB)
- Single Thread
- Hỗ trợ nhiều kiểu dữ liệu low-level (Hash, List, Set, …)
- Giúp hệ thống chịu tải tốt hơn -> Nâng cao High Avaibility

# II. Cơ chế hoạt động
- Khi client kết nối Server, Redis đăng ký socket của client với OS kernel thông qua API IO multiplexing
- Khi client gửi data, OS kernel phát hiện socket sẵn sàng và thông báo cho Redis
- API IO multiplexing là cơ chế do OS kernel cung cấp (ví dụ: epoll trên Linux, IOCP trên Windows)

![alt text](images/operation_mechanism.png)

# III. Drawback
- Giới hạn dung lượng do dữ liệu lưu trong RAM
- Chủ yếu sử dụng 1 core CPU
- Không phù hợp làm database chính cho dữ liệu lâu dài