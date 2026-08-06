#!/bin/bash

SSH_KEY="$HOME/Downloads/ssh-key-2026-02-14.key"
SERVER_IP="170.9.254.97"

echo "========================================="
echo "COMPREHENSIVE BOT AUDIT"
echo "Server: $SERVER_IP"
echo "========================================="

ssh -i "$SSH_KEY" ubuntu@$SERVER_IP << 'ENDSSH'

BOTS=("cbot" "clawdbot" "credit_spread_bot" "ob-bot")

for bot in "${BOTS[@]}"; do
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🤖 BOT: $bot"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    if [ -d "$HOME/$bot" ]; then
        cd "$HOME/$bot"
        
        # Basic Info
        echo "📁 Location: $HOME/$bot"
        echo "📊 Size: $(du -sh . | cut -f1)"
        echo "📅 Last Modified: $(stat -c %y . 2>/dev/null | cut -d. -f1)"
        
        # Check if running
        echo ""
        echo "🔄 Status:"
        if pgrep -f "$bot" > /dev/null; then
            echo "   ✅ CURRENTLY RUNNING"
            echo "   Process details:"
            ps aux | grep -v grep | grep "$bot" | sed 's/^/   /'
        else
            echo "   ❌ NOT RUNNING"
        fi
        
        # Directory structure
        echo ""
        echo "📂 Directory Structure:"
        tree -L 2 -I 'venv|__pycache__|node_modules|.git' . 2>/dev/null || ls -lah | sed 's/^/   /'
        
        # Find README or docs
        echo ""
        echo "📖 Documentation:"
        if ls README* 2>/dev/null; then
            echo "   Found README:"
            cat README* | head -20 | sed 's/^/   /'
        else
            echo "   ⚠️  No README found"
        fi
        
        # Check main Python file for clues
        echo ""
        echo "🐍 Main Script Analysis:"
        MAIN_FILE=""
        if [ -f "main.py" ]; then
            MAIN_FILE="main.py"
        elif [ -f "bot.py" ]; then
            MAIN_FILE="bot.py"
        elif [ -f "app.py" ]; then
            MAIN_FILE="app.py"
        fi
        
        if [ -n "$MAIN_FILE" ]; then
            echo "   Main file: $MAIN_FILE"
            echo "   Description from code:"
            head -30 "$MAIN_FILE" | grep -E "^#|'''|\"\"\"" | sed 's/^/   /'
            echo ""
            echo "   Key imports:"
            grep "^import\|^from" "$MAIN_FILE" | head -10 | sed 's/^/   /'
        fi
        
        # Check requirements
        echo ""
        echo "📦 Dependencies:"
        if [ -f "requirements.txt" ]; then
            echo "   requirements.txt (first 10 lines):"
            head -10 requirements.txt | sed 's/^/   /'
        fi
        
        # Check config files
        echo ""
        echo "⚙️  Configuration Files:"
        ls -lh .env* config.* settings.* *.json *.yaml *.yml 2>/dev/null | sed 's/^/   /'
        
        # Check for API keys/credentials (without exposing them)
        echo ""
        echo "🔑 Credentials Check:"
        if [ -f ".env" ]; then
            echo "   .env file exists - Keys found:"
            grep -E "API|KEY|SECRET|TOKEN|PASSWORD" .env | cut -d'=' -f1 | sed 's/^/   - /'
        fi
        
        # Check logs for activity
        echo ""
        echo "📝 Recent Activity:"
        LOG_FILE=$(ls -t *.log 2>/dev/null | head -1)
        if [ -n "$LOG_FILE" ]; then
            echo "   Last log: $LOG_FILE"
            echo "   Last modified: $(stat -c %y "$LOG_FILE" 2>/dev/null | cut -d. -f1)"
            echo "   Last 5 entries:"
            tail -5 "$LOG_FILE" | sed 's/^/   /'
            echo ""
            echo "   First 5 entries (to see when it started):"
            head -5 "$LOG_FILE" | sed 's/^/   /'
        else
            echo "   ⚠️  No logs found - likely never run or logs cleared"
        fi
        
        # Check cron jobs
        echo ""
        echo "⏰ Scheduled Tasks:"
        crontab -l 2>/dev/null | grep "$bot" | sed 's/^/   /' || echo "   No cron jobs found"
        
        # Check systemd services
        echo ""
        echo "🔧 System Services:"
        systemctl list-units --type=service --all | grep "$bot" | sed 's/^/   /' || echo "   No systemd services found"
        
        # Disk usage breakdown
        echo ""
        echo "💾 Disk Usage by Directory:"
        du -sh * 2>/dev/null | sort -hr | head -5 | sed 's/^/   /'
        
    else
        echo "❌ Directory not found: $HOME/$bot"
    fi
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
done

# Overall system info
echo ""
echo "========================================="
echo "📊 SYSTEM OVERVIEW"
echo "========================================="
echo "Total disk usage by bots:"
du -sh ~/cbot ~/clawdbot ~/credit_spread_bot ~/ob-bot 2>/dev/null | sort -hr

echo ""
echo "All Python processes:"
ps aux | grep python | grep -v grep

echo ""
echo "Disk space:"
df -h ~

ENDSSH

echo ""
echo "========================================="
echo "✅ Audit Complete"
echo "========================================="
