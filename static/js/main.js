document.addEventListener('DOMContentLoaded', function() {
    
    // --- 暗色模式切换 ---
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    
    // 初始化时检查本地存储
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
    }

    darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        // 将偏好保存到本地存储
        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
        } else {
            localStorage.setItem('darkMode', 'disabled');
        }
    });
});