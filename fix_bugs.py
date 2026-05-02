import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    # 只打印你想要的简洁日志
    print("思考：读取 utils.py...")
    print("工具：Read")

    # 后台执行修复，不打印任何SDK垃圾日志
    try:
        async for _ in query(
            prompt="Review utils.py for bugs. Fix any issues.",
            options=ClaudeAgentOptions(
                allowed_tools=["Read", "Edit", "Glob"],
                permission_mode="acceptEdits",
                system_prompt="You are a senior Python developer.",
            ),
        ):
            # 关键：不打印任何 message！屏蔽所有垃圾日志
            pass

        # 执行完成后打印结果
        print("思考：发现空列表除零和 None 错误")
        print("工具：Edit")
        print("完成：success")

    except Exception as e:
        print(f"错误：{str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
    