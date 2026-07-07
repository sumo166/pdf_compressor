import os
import sys
import fitz
from pathlib import Path

def compress_pdf(input_path, output_path, target_size_mb=5):
    doc = fitz.open(input_path)
    original_size = os.path.getsize(input_path) / (1024 * 1024)
    
    if original_size <= target_size_mb:
        doc.save(output_path, garbage=4, deflate=True, clean=True)
        doc.close()
        return original_size, original_size, 0.0
    
    target_size_bytes = target_size_mb * 1024 * 1024
    temp_dir = Path(output_path).parent / "pdf_compress_temp"
    temp_dir.mkdir(exist_ok=True)
    
    quality_levels = [90, 80, 70, 60, 50, 40, 35, 30, 25, 20]
    final_size = original_size
    
    for quality in quality_levels:
        doc_new = fitz.open()
        
        for page_num in range(doc.page_count):
            page = doc[page_num]
            pix = page.get_pixmap(alpha=False)
            
            temp_img = str(temp_dir / f"page_{page_num}.jpg")
            pix.save(temp_img, jpg_quality=quality)
            
            img_pix = fitz.Pixmap(temp_img)
            new_page = doc_new.new_page(width=img_pix.width, height=img_pix.height)
            new_page.insert_image(new_page.rect, filename=temp_img)
        
        doc_new.save(output_path, garbage=4, deflate=True, clean=True)
        doc_new.close()
        
        current_size = os.path.getsize(output_path)
        current_size_mb = current_size / (1024 * 1024)
        final_size = current_size_mb
        
        if current_size <= target_size_bytes:
            break
    
    for f in temp_dir.glob("*.jpg"):
        f.unlink()
    temp_dir.rmdir()
    
    doc.close()
    reduction = ((original_size - final_size) / original_size) * 100
    return original_size, final_size, reduction

def main():
    if len(sys.argv) < 2:
        print("使用方法:")
        print("python pdf_compressor.py <PDF文件1> [<PDF文件2> ...]")
        print("示例:")
        print("python pdf_compressor.py file1.pdf file2.pdf")
        sys.exit(1)
    
    pdf_files = sys.argv[1:]
    results = []
    
    for pdf_path in pdf_files:
        if not os.path.exists(pdf_path):
            print(f"错误: 文件 '{pdf_path}' 不存在")
            continue
        
        if not pdf_path.lower().endswith('.pdf'):
            print(f"跳过: '{pdf_path}' 不是PDF文件")
            continue
        
        output_path = str(Path(pdf_path).parent / (Path(pdf_path).stem + "_compressed.pdf"))
        
        original, final, reduction = compress_pdf(pdf_path, output_path)
        results.append({
            'file': Path(pdf_path).name,
            'original': original,
            'final': final,
            'reduction': reduction
        })
    
    print("\n压缩完成！")
    print("=" * 60)
    print(f"{'文件名':<30} {'原始大小':>10} {'压缩后':>10} {'压缩率':>8}")
    print("=" * 60)
    for res in results:
        print(f"{res['file']:<30} {res['original']:>9.2f} MB {res['final']:>10.2f} MB {res['reduction']:>7.1f}%")
    print("=" * 60)

if __name__ == "__main__":
    main()