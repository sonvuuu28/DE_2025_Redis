# I. Redis
- Inmemory-Database (Nhanh hơn Disk-DB)
- Single Thread
- Hỗ trợ nhiều kiểu dữ liệu low-level (Hash, List, Set, …)
- Giúp hệ thống chịu tải tốt hơn (Lớp bảo vệ) -> Nâng cao High Avaibility

# II. Cơ chế hoạt động
- Khi client kết nối Server, Redis đăng ký socket của client với OS kernel thông qua API IO multiplexing
- Khi client gửi data, OS kernel phát hiện socket sẵn sàng và thông báo cho Redis
- API IO multiplexing là cơ chế do OS kernel cung cấp (ví dụ: epoll trên Linux, IOCP trên Windows)

![alt text](images/operation_mechanism.png)

# III. Lưu ý
- Không thay database truyền thống
- Restart server, data trong Redis sẽ mất -> cần cấu hình persistency
- Nhất quán dữ liệu: Ghi vào Redis trước hay DB khác trước hay cùng lúc
- Redis Cluster cải thiện điểm yếu 1 luồng