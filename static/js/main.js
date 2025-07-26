// /js/main.js

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

    // --- 语言切换器逻辑 ---
    const langSwitcher = document.getElementById('lang-switcher');
    if (langSwitcher) {
        const currentPath = window.location.pathname;
        const currentLang = document.documentElement.lang.startsWith('zh') ? 'zh' : 'en';
        const otherLang = currentLang === 'en' ? 'zh' : 'en';

        // 构造目标语言的对应页面路径
        let targetPath;
        if (currentPath.startsWith(`/${currentLang}/`)) {
            targetPath = currentPath.replace(`/${currentLang}/`, `/${otherLang}/`);
        } else {
            // 处理根目录跳转后的情况
            targetPath = `/${otherLang}/${currentPath.substring(1)}`;
        }
        
        // 如果在根目录（比如跳转前的 index.html），则直接指向目标语言首页
        if (currentPath === '/' || currentPath === '/index.html') {
             targetPath = `/${otherLang}/`;
        }

        langSwitcher.href = targetPath;
    }

});